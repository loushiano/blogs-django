from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Create your models here.

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "role"


class Category(models.Model):
    id = models.AutoField(primary_key=True, db_column="category_id")
    name = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "category"


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField('email_address', unique=True, null=True)
    first_name = models.CharField('first_name', max_length=30, null=True)
    last_name = models.CharField('last_name', max_length=30, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    password = models.TextField()
    REQUIRED_FIELDS = ('password',)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = "blog_user"


class Blog(models.Model):
    id = models.AutoField(primary_key=True, db_column="blog_id")
    text = models.TextField(null=True)
    title = models.CharField(max_length=255, null=True, unique=True)
    date_created = models.DateField(null=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_column="user_id", related_name="blogs")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, db_column="category_id")

    class Meta:
        db_table = "blog"





