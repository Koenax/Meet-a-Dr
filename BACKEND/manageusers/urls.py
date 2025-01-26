from django.urls import path
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from django.http import JsonResponse

def auth_root_view(request):
    return JsonResponse({
        "message": "API Authentication Endpoints",
        "endpoints": [
            "/register/ - Register a new user",
            "/login/ - Log in a user", # LoginView: Endpoint for user login.
            "/logout/ - Log out the user",
            "/user/ - Get user details",
            "/token/verify/ - Verify a JWT token",
            "/token/refresh/ - Refresh a JWT token"
        ]
    })

urlpatterns = [
    path('', auth_root_view, name='auth_root'),  # Root endpoint
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
