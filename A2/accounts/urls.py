from django.urls import path
urlpatterns = [
    path('register/',view.register_view,name="register"),
    path('login/',view.login_view,name="login"),
    path('logout/',view.logout_view,name="logout"),
    path('profile/view/',view.profile_view,name="profile_view"),
    path('profile/edit/',view.profile_edit,name="profile_edit")
]
