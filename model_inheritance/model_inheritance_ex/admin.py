from django.contrib import admin
from .models import Employee ,Customer , GrandFather ,Father ,Son



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','loc' ,'sal' ,'mobile']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name' ,'loc' ,'email' ,'age']


class GrandAdmin(admin.ModelAdmin):
    list_display = ['gname','age']

class FatherAdmin(admin.ModelAdmin):
    list_display = ['fname','job']

class SonAdmin(admin.ModelAdmin):
    list_display = ['sname','course']


admin.site.register(GrandFather ,GrandAdmin)
admin.site.register(Father,FatherAdmin)
admin.site.register(Son ,SonAdmin)
admin.site.register(Employee ,EmployeeAdmin)
admin.site.register(Customer ,AdminCustomer)















