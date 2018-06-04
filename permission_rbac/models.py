from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    roles = models.ManyToManyField(to="Role")

    def __str__(self): return self.name

    class Meta:
        verbose_name = "用户表"
        db_table = verbose_name


class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(to="Permission")

    def __str__(self): return self.title

    class Meta:
        verbose_name = "角色表"
        db_table = verbose_name


class Permission(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    action=models.CharField(max_length=100,default="")
    group=models.ForeignKey("PermissionGroup",default=1)

    def __str__(self): return self.title
    class Meta:
        verbose_name = "权限表"
        db_table = verbose_name


class PermissionGroup(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self): return self.title
    class Meta:
        verbose_name = "分组表"
        db_table = verbose_name