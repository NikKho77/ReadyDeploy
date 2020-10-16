from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Audio,Contacts,Gallery,Main,Onas,Repertuar,RepertuarMan,RepertuaWomen,Video,Index
# Create your views here.

class AudioView(ListView):
    model = Audio
    template_name = 'audio.html'

class ContactsView(ListView):
    model = Contacts
    template_name = 'contacts.html'

class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery.html'

class MainView(ListView):
    model = Main
    template_name = 'main.html'

class OnasView(ListView):
    model = Onas
    template_name = 'Onas.html'

class RepertuarView(ListView):
    model = Repertuar
    template_name = 'repertuar.html'

class RepertuarManView(ListView):
    model = RepertuarMan
    template_name = 'repertuarMan.html'

class RepertuarWomenView(ListView):
    model = RepertuaWomen
    template_name = 'repertuarWomen.html'

class VideoView(ListView):
    model = Video
    template_name = 'video.html'

class IndexView(ListView):
    model = Index
    template_name = 'index.html'