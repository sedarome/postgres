from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    #edate = models.DateField(auto_now=False,auto_now_add=True)
    ename = models.CharField(max_length=100)
    #ename = models.FileField()
    #ename = models.TextField()
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "evento"
