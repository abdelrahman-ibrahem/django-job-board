from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
TYPES = (
    ('f' , 'full-time'),
    ('p' , 'part-time'),
)
class Job(models.Model):
    user = models.ForeignKey(User , related_name="owner_job", on_delete=models.CASCADE , blank=True , null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='jobs/')
    job_type = models.CharField(choices=TYPES , max_length=200)
    descrption = models.TextField(max_length=400)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    experiance = models.IntegerField()
    slug = models.SlugField(max_length=200 , blank=True , null=True)
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title



class Contact(models.Model):
    message = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('contact')
        verbose_name_plural = ('contacts')
    
    def __str__(self):
        return self.name
    



class ApplForJob(models.Model):
    name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    website = models.URLField(max_length = 200 , blank=True , null=True)
    cv = models.FileField(upload_to='cvs', max_length = 100, blank=True , null=True)
    cover = models.TextField(max_length=260, blank=True , null=True)

    def __str__(self):
        return str(self.name)
    
