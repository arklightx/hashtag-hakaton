from django.contrib import admin
from django.urls import path, include

"""
/api
    GET /course
    GET /course/id(type int)
    POST /course
    DELETE /course
    PATCH/PUT /course
    GET /parent
    PATCH/PUT /parent
    DELETE /parent (?)
    GET /teacher
    GET /schedule?id=type int
/accounts 
    POST /sign_in
    POST /sign_up
    POST /logout
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
    #  /auth/users/ - register
    #  /auth/token/login/
    #  /auth/token/logout/
]
