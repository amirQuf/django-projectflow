from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "email",
            "last_name",
            "avatar",
            "bio",
            "github_link",
            "portfolio_link",
            "is_active",
        ]
