from django.urls import path
from apis import views

urlpatterns = [
    path('apis/', views.project_list),
    path('apis/<int:pk>/', views.project_detail),
]