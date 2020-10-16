from django.db import models

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Contacts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Main(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Onas(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Repertuar(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class RepertuarMan(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class RepertuaWomen(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Video(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Index(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()