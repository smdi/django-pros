from django.db import models

'''

abstract inheritance

'''

class Common(models.Model):
    name = models.CharField(max_length=20)
    loc  = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Employee(Common):
    sal  = models.IntegerField()
    mobile = models.BigIntegerField()
    def __str__(self):
        return self.name


class Customer(Common):
    age  =  models.IntegerField()
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name

'''

multi table inheitance

'''

class GrandFather(models.Model):
    gname = models.CharField(max_length=20)
    age   = models.IntegerField()
    def __str__(self):
        return self.gname




class Father(GrandFather):
    fname = models.CharField(max_length=20)
    job   = models.CharField(max_length=20)
    def __str__(self):
        return self.fname


class Son(Father):
    sname = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    def __str__(self):
        return self.sname









