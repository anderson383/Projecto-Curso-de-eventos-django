from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager,models.Manager):
    def _create_user(self,username, email, password,
                      is_staff, is_superuser,**extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,is_active=True, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        #guarda usuario especificando la base de datos actual
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email,password=None,**extra_fields):
        return self._create_user(username,email,password,False,False,**extra_fields)
    
    def create_superuser(self, username, email,password=None,**extra_fields):
        return self._create_user(username,email,password,True,True,**extra_fields)
    
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="users")
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = "Usuario"