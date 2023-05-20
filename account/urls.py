from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import MyObtainTokenPairView, RegisterView, ProfileView, SendEmailVerificationCodeView, \
    CheckEmailVerificationCodeView, VerificationCodeWithParams

urlpatterns = [
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", VerificationCodeWithParams.as_view(), name="check-email"),
]
