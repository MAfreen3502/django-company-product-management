from django.db import models
from django.urls import reverse


# Create your models here.
class Company(models.Model):
    companyName=models.CharField(max_length=100)
    Ceo=models.CharField(max_length=100)
    est_year=models.PositiveIntegerField()
    origin=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='logo/',null=True,blank=True)

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk':self.pk})

   
    def __str__(self):
        return self.companyName

    


class Product(models.Model):
    productName=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    seat_capacity = models.PositiveIntegerField()
    fuel_type=models.CharField(max_length=100)
    cc=models.CharField(max_length=100)
    miliege=models.PositiveIntegerField()
    price=models.PositiveBigIntegerField()
    prod_img=models.ImageField(upload_to='pimg/',null=True,blank=True)
  
    company=models.ForeignKey(Company,on_delete=models.CASCADE, related_name="companies")

    def __str__(self):
        return self.productName

    
        
