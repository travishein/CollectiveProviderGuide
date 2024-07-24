from django.urls import path

from .views import ThcnpLoginView, ThcnpSignUpView, dashboard, index

urlpatterns = [
    path("login/", ThcnpLoginView.as_view(), name="thcnp_login"),
    path("signup/", ThcnpSignUpView.as_view(), name="thcnp_signup"),
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]
