from django.urls import path

from cartapp import views

app_name = 'cartapp'

urlpatterns = [

    path('', views.allprodcat, name='allprodcat'),
    path('shop/<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:p_slug>',views.prodetail,name='prodetail'),

]
