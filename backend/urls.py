from django.urls import path

from backend.views import add_user, show_users,delete_all_users

urlpatterns = [
    path("add_user", add_user),
    path("show_users", show_users),
    path("delete_all_users", delete_all_users)
]