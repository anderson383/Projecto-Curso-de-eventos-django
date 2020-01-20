from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings
# Create your models here.
class TimeStandModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        #Definir que la clase es abstracta 
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Categoria"
class Event(TimeStandModel):
    name      =  models.CharField(max_length=200, unique=True)
    slug      =  models.SlugField(editable=False)
    summary   =  models.TextField(max_length=255)
    content   =  models.TextField()
    category  =  models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    place     =  models.CharField(max_length=50)
    start     =  models.DateTimeField()
    finish    =  models.DateTimeField()
    image     =  models.ImageField( upload_to="events") 
    is_free   =  models.BooleanField(default=True)
    amount    =  models.DecimalField( max_digits=5, decimal_places=2)
    views     =  models.PositiveIntegerField(default=0)
    organizer =  models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Event, self).save(*args,**kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Evento"
class Assistant(TimeStandModel):
    assistand = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="", on_delete=models.CASCADE)
    event =  models.ManyToManyField(Event, verbose_name="")
    
    attended = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s  %s" % (self.assistand, self.event)
    class Meta:
        verbose_name = "Asistente"
class Comments(TimeStandModel):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name="", on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return "%s %s" % (self.user, self.event)
    class Meta:
        verbose_name = "Comentarios"
    