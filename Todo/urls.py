from django.urls import path
from .views import *

# Simple function to return a response for "/"

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('sign-in/', sign_in, name="sign_in"),
    path('sign-up/', sign_up, name="sign_up"),
    path('send-reset-link/', send_reset_link, name="send_reset_link"),
    path('auth/reset-password/<uidb64>/<token>/', update_password, name='reset-password'),
    path('check-workspace-count/', check_workspaces_count, name="check_workspaces_count"),
    path('add-workspace/', add_workspace, name="create_workspace"),
    path('get-mail/', get_mail, name="get_mail"),
]
