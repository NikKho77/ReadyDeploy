from django.urls import path, include
from . import views
from .views import AudioView,ContactsView,GalleryView,MainView,OnasView,RepertuarView,RepertuarManView,RepertuarWomenView,VideoView,IndexView

urlpatterns = [
  #  path('', views.home, name="home"),

    path('audio.html/', AudioView.as_view(), name="audio"),
    path('contacts.html/', ContactsView.as_view(), name="contacts"),
    path('gallery.html/', GalleryView.as_view(), name="gallery"),
    path('Onas.html/' , OnasView.as_view(), name="Onas"),
   # path('', MainView.as_view(), name = "main"),
    path('repertuar.html/', RepertuarView.as_view(), name = "repertuar"),
    path('repertuarMan.html/', RepertuarManView.as_view(), name = "repertuarMan"),
    path('repertuarWomen.html/', RepertuarWomenView.as_view(), name = "repertuarWomen"),
    path('video.html/', VideoView.as_view(), name = "video"),
    path('', MainView.as_view(), name = "main"),
    path('', IndexView.as_view(), name = "index"),




]