from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
class Manager(UserManager):

    def create_user(self, first_name, last_name, username, email, password=None):

        if not email :
            ValueError('user must have an email address ! ')

        if not username :
            ValueError('user must have a username ! ')

        user =self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user =self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self.db)

        return user 




class User(AbstractUser):

      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      username = models.CharField(max_length=50,unique=True)
      email = models.EmailField(unique=True)

      date_joined = models.DateField(auto_now_add=True)
      last_login = models.DateField(auto_now=True)

      is_admin = models.BooleanField(default=False)
      is_staff = models.BooleanField(default=False)
      is_active = models.BooleanField(default=False)
      is_superadmin = models.BooleanField(default=False)

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username','first_name','last_name']

      objects = Manager()

      def __str__(self):
          return self.email

      def has_perm(self , perm, obj=None):
          return self.is_admin

      def has_module_perms(self, add_label):
           return True