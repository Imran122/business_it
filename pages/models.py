from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from random import random
from django.urls import reverse
from django.db.models.signals import pre_save
# Create your models here.


class Categorey(models.Model):
    title = models.CharField(max_length=70)


    def __str__(self):
        return self.title
 
    
class Works(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    categories = models.ForeignKey(Categorey,on_delete=models.CASCADE)
    overview = models.TextField(max_length=400)
    content = RichTextField()
    clients = models.CharField(max_length=100,null=True, blank=True)
    clientsAddress = models.CharField(max_length=200,null=True,blank=True)
    projectUrl = models.CharField(max_length=150,null=True,blank=True)
    projectGithub = models.CharField(max_length=150,null=True,blank=True)
    projectDelevery = models.DateTimeField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    postimage1 = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    postimage2 = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    postimage3 = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    file = models.FileField(upload_to='file',null=True)
    is_published = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('details',kwargs={ 'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Works.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_details_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_details_receiver, Works)





class Contact(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    email_from = models.EmailField(blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    title = models.CharField(max_length=150)
    client_name = models.CharField(max_length=100)
    message = models.TextField(max_length=500,null=True,blank=True)
    images = models.ImageField(upload_to='photos/client/%Y/%m/%d',null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    site_url = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.title