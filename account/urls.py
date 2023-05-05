from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import MyObtainTokenPairView, RegisterView

urlpatterns = [
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
