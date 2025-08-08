from django.urls import path,include
from .views import show_all_users,show_specific_user,delete_user,add_user,update_user,contact_view,thank_you_view

urlpatterns = [
    path("add/",add_user,name="add_user"),
    path("all_user/",show_all_users,name="all_user"),
    path("specific_user/<int:pk>",show_specific_user,name="specific_user"),
    path("delete/<int:pk>/", delete_user, name="delete_user"),
    path("update/<int:pk>",update_user,name="update_user"),
    path("contact/",contact_view,name="contact"),
    path("thank_you/",thank_you_view,name="thank_you"),
]