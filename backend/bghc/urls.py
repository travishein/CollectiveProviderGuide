from django.urls import path

from .views import BghcLoginView, BghcSignUpView, dashboard, index

urlpatterns = [
    path("login/", BghcLoginView.as_view(), name="bghc_login"),
    path("signup/", BghcSignUpView.as_view(), name="bghc_signup"),
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]
