from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    work = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    ytlink = models.TextField(null=True, blank=True)
    myimg = models.ImageField(upload_to='photos',null=True, blank=True)
    aboutimg1 = models.ImageField(upload_to='photos',null=True, blank=True)
    aboutimg2 = models.ImageField(upload_to='photos',null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skill = models.CharField(max_length=100, null=True, blank=True)
    links = models.TextField(null=True, blank=True)
    thumb = models.ImageField(upload_to='project',null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icons = models.ImageField(upload_to='skill',null=True, blank=True)
    skillicon = models.ImageField(upload_to='skill',null=True, blank=True)
    
    def __str__(self):
        return self.name