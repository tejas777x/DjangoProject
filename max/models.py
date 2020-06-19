from django.db import models

from django.contrib.auth.models import User


# creating UserProfileInfo model
class UserProfileInfo(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)  # deleting the user details when user is deleted
     mobile_no = models.IntegerField()  # datatype of mobile number field
     address = models.CharField(max_length=500)  # datatype of address field

     # to convert your object to string
     def __str__(self):
        return str(self.user.username)


# creating Name model
class Name(models.Model):
    item_name = (models.CharField(max_length=120))  # datatype of item_name field

    # to convert your object to string
    def __str__(self):
        return str(self.item_name)

# creating Electronics model
class Electronics(models.Model):

    name_type = models.ForeignKey(Name, default=Name, on_delete=models.CASCADE)  # datatype of name_type field with a foreign key to connect to the Name module
    item_id = models.CharField(max_length=120)  # datatype of item_id field
    specification = models.CharField(max_length=120)   # datatype of specification field

    # to convert your object to string
    def __str__(self):
        return str(self.item_id) + '-' + str(self.name_type) + '-' + str(self.specification)

# creating Seller model
class Seller(models.Model):
    srno= models.IntegerField() # datatype of srno field
    model_seller = models.ForeignKey(Electronics, default= Electronics, on_delete=models.CASCADE)  # datatype of model_seller field with a foreign key to connect to the Electronics module
    name = models.CharField(max_length=120)  # datatype of name field
    address = models.CharField(max_length=120)   # datatype of address field
    email_id = models.CharField(max_length=120)  # datatype of email_id field
    price = models.IntegerField()   # datatype of price field

    # to convert your object to string
    def __str__(self):
        return str(self.model_seller) + '-' + str(self.name) + '-' + str(self.address) + '-' + str(self.email_id) + '-' + str(self.price)
