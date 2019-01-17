from django.db import models

# Create your models here.

#
# class Student(models.Model):
#     sname =  models.CharField(max_length= 20)
#     loc   =  models.CharField(max_length= 20)
#     age   = models.IntegerField()
#     email = models.EmailField(max_length=40)
#     def __str__(self):
#         return self.sname
#
# class Course(models.Model):
#     student = models.OneToOneField(Student,on_delete=models.DO_NOTHING)
#     cname   = models.CharField(max_length=20)
#     fee     = models.IntegerField()
#     def __str__(self):
#         return self.cname

#
# class Student(models.Model):
#     sname =  models.CharField(max_length= 20)
#     loc   =  models.CharField(max_length= 20)
#     age   = models.IntegerField()
#     email = models.EmailField(max_length=40)
#     def __str__(self):
#         return self.sname
#
# class Course(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
#     cname   = models.CharField(max_length=20)
#     fee     = models.IntegerField()
#     def __str__(self):
#         return self.cname
#



class Author(models.Model):
    aname =  models.CharField(max_length= 20)
    loc   =  models.CharField(max_length= 20)
    def __str__(self):
        return  self.aname



class Book(models.Model):
    author = models.ManyToManyField(Author )
    bname  = models.CharField(max_length= 20)
    bcost  = models.IntegerField()
    def __str__(self):
        return self.bname

    def get_authors(self):
        return "\n".join([p.aname for p in self.author.all()])








