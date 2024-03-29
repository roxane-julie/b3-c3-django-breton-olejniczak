"""
URL configuration for passwordManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUp, name='signUp'),
    path('signin/', views.signIn, name='signIn'),
    path('success/', views.success, name='success'),
    path('manager/', views.myPasswordsManager, name='myPasswordsManager'),
    path('manager/safeBoxContainer/', views.safeBoxContainer, name='safeBoxContainer'),
    path('manager/deleteSafebox/<int:safebox_id>/', views.deleteSafebox, name='deleteSafebox'),
    path('manager/safeBoxContainer/getPasswordData/<int:password_data_id>/', views.getPasswordData, name='getPasswordData'),
    path('manager/safeBoxContainer/deleteCard/<int:password_data_id>/', views.deleteCard, name='deleteCard'),
    path('manager/safeBoxContainer/updateField/<str:field_name>/<int:id_value>/', views.updateField, name='updateField'),
    path('import_from_csv/<int:safebox_id>/', views.import_from_csv, name='import_from_csv'),
     path('export_to_csv/', views.export_to_csv, name='export_to_csv'),
    path('createNewCard/', views.createNewCard, name='createNewCard'),
    path('signout/', views.signOut, name='signOut'),
]
