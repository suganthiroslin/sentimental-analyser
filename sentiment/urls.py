from django.urls import path
from . import views


urlpatterns = [

    # ==================== HOME ====================

    path(
        '',
        views.home,
        name='home'
    ),


    # ==================== ABOUT ====================

    path(
        'about/',
        views.about,
        name='about'
    ),


    # ==================== LOGIN ====================

    path(
        'login/',
        views.login_view,
        name='login'
    ),


    # ==================== REGISTER ====================

    path(
        'register/',
        views.register_view,
        name='register'
    ),


    # ==================== LOGOUT ====================

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),


    # ==================== SENTIMENT API ====================

    path(
        'api/analyze/',
        views.analyze_api,
        name='analyze_api'
    ),

]
