from django.urls import path
from .import views 
from .views import UserRegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.homeVIEW, name='home'),
  path('home',views.livehomeVIEW, name='livehome'),
  path('sloat',views.cardVIEW, name='card'),
  path('Details/<int:id>',views.detailsVIEW, name='details'),
  path('myenrolls/',views.enrollsVIEW, name='class'),
  path('account/',views.accountVIEW, name='account'),
  path('class/<int:id>',views.classmetarialVIEW, name='tclass'),
  path('register',UserRegisterView.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
