from datetime import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.models import VerificationOtp
from auth.serializers import UserCreateSerializer
from users.models import CustomUser


class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user = CustomUser.objects(email=validated_data.get("email"), is_active=False).first()
        if user is not None:
            try:
                sms = VerificationOtp.object.get(
                    user=user,
                    type=VerificationOtp.VerificationType.REGISTER,
                    expires_in__lt = timezone.now(),
                    is_active=True
                )
            except VerificationOtp.DoesNotExist:
                user.set_password(validated_data.get('password'))
                user.save()
        else:
            user = CustomUser.objects.create(
                first_name=validated_data.get('first_name'),
                last_name=validated_data.get('last_name'),
                email=validated_data.get('email')
            )
            user.set_password(validated_data.get('password'))
            user.save()
        return Response({"message": "User created or updated successfully"}, status=status.HTTP_201_CREATED)

