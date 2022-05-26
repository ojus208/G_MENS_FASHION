from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home" ),
    path('category/<title>', views.category, name="category"),
    path('product_type/<title>', views.type, name="product_type"),
    path('brands/<title>', views.brand, name="brands"),
    path('search/', views.search, name="search" ),
    path('cart/', views.cart, name="cart" ),
    path('favorite/', views.favorite, name="favorite" ),
    path('product/<title>', views.product, name="product" ),
    path("user/", views.user, name="user" ),
    path("login/", views.login, name="login" ),
    path("logout/", views.logout, name="logout" ),
    path("signup/", views.signup, name="signup" ),
    path("otp/", views.otp, name="otp" ),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)