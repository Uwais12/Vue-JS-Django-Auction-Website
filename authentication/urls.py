from django.urls import path
from . import views

app_name = "authenticate"

urlpatterns = [

    # register page
    path("register/", views.registerPage, name="register"),

    # login page
    path("login/", views.loginPage, name="login"),

    # logout page
    path("logout/", views.logout, name="logout"),

    # main page - containing the items listed
    path("api/products", views.products_api, name="productsapi"),

    # details for the details for a product
    path("api/products/<int:product_id>", views.product_api, name="productapi"),

    # path to display the messages for every post
    path("api/messages", views.messages_api, name="messagesapi"),

    # path to display the responses for every message
    path("api/responses", views.responses_api, name="responsesapi"),

    # path for profile page
    path("api/profile", views.profile, name="profile"),

    # path that redirects to the details of the profile page
    path("api/profile/<int:profile_id>", views.profile_api, name="profile_api"),
]
