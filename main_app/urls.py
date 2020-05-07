from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bats/', views.bats_index, name='index'),
    path('bats/<int:bat_id>/', views.bats_detail, name='detail'),
    path('bats/create/', views.BatCreate.as_view(), name='bats_create'),
    path('bats/<int:pk>/update/', views.BatUpdate.as_view(), name='bats_update'),
    path('bats/<int:pk>/delete/', views.BatDelete.as_view(), name='bats_delete'),
    path('bats/<int:bat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('bats/<int:bat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),   
    path('accounts/signup/', views.signup, name='signup'),
]