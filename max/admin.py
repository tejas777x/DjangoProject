from django.contrib import admin
from .models import Electronics  # to import Electronics model
from .models import Seller  # to import Seller model
from  .models import Name  # to import Name model
from.models import UserProfileInfo, User  # to import UserProfileInfo model
admin.site.register(Electronics)  # to display your Electronics models in django admin pannel
admin.site.register(Seller)  # to display your Seller models in django admin pannel
admin.site.register(Name)  # to display your Name models in django admin pannel
admin.site.register(UserProfileInfo)  # to display your UserProfileInfo models in django admin pannel
