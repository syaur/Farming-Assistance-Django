from django.urls import path
from dealer import views


urlpatterns = [
    path('',views.deshboard,name='deshboard'),
    path('addcategory/', views.addcategory, name = 'addcategory'),
    path('addproduct/', views.addproduct, name = 'addproduct'),
    # path('product/', views.display, name = 'displayproduct'),
    path('addad/', views.addad, name='addad')
]