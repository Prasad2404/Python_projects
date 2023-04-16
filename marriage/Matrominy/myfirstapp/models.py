from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):   #done
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile_photo=models.FileField(upload_to='media/profile_photo',null=True,blank=True)
    primary_contact=models.CharField(max_length=10)
    alternate_contact=models.CharField(max_length=10)
    dob=models.DateTimeField(max_length=10)
    mother_tounge=models.CharField(max_length=10)
    location=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    marital_status=models.CharField(max_length=10)
    about_profile=models.CharField(max_length=100)
    main_origin=models.CharField(max_length=50)
    otp=models.PositiveIntegerField()
    update_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


    family_info=models.OneToOneField('Family_info',on_delete=models.CASCADE,null=True,blank=True)
    address=models.OneToOneField('Address',on_delete=models.CASCADE,null=True,blank=True)
    religious=models.OneToOneField('Religious',on_delete=models.CASCADE,null=True,blank=True)
    professional_detail=models.OneToOneField('Professional_detail', on_delete=models.CASCADE, null=True, blank=True)
    customer_expectation=models.OneToOneField('Customer_expectation',on_delete=models.CASCADE,null=True,blank=True)
    physical_details=models.OneToOneField('Physical_details',on_delete=models.CASCADE,null=True,blank=True)
    photo_id=models.OneToOneField('Photo_id',on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return str(self.primary_contact)

class Family_info(models.Model):
    total_member_in_family=models.PositiveIntegerField(null=True,blank=True)
    relationship=models.CharField(max_length=20)
    married_status=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    family_type=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    update_at=models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    citizenship=models.CharField(max_length=20,null=True,blank=True)
    address_type = models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    update_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Religious(models.Model):      #done
    religion=models.CharField(max_length=20)
    caste=models.CharField(max_length=20)
    subcaste=models.CharField(max_length=20)
    star = models.CharField(max_length=20)
    rashi=models.CharField(max_length=20)
    dosh=models.CharField(max_length=20)
    manglik=models.CharField(max_length=20)
    religious_update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Professional_detail(models.Model):    #done
    heighst_education=models.CharField(max_length=20)
    heighst_educatio_stream=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    office_address=models.CharField(max_length=20)
    annual_income=models.CharField(max_length=20)
    professional_detail_update_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Customer_expectation(models.Model):
    exp_min_age=models.IntegerField()
    exp_max_age=models.IntegerField()
    exp_height=models.FloatField(max_length=20)
    exp_marital_status=models.CharField(max_length=20)
    exp_mother_tounge=models.CharField(max_length=20)
    exp_eating_habit=models.CharField(max_length=20)
    exp_smoking_habbit=models.CharField(max_length=20)
    exp_drinking_habbit=models.CharField(max_length=20)
    exp_religion=models.CharField(max_length=20)
    exp_caste=models.CharField(max_length=20)
    exp_subcaste = models.CharField(max_length=20)
    exp_star = models.CharField(max_length=20)
    exp_dosh = models.CharField(max_length=20)
    exp_rashi = models.CharField(max_length=20)
    exp_mangalik = models.CharField(max_length=20)
    exp_education = models.CharField(max_length=20)
    exp_city = models.CharField(max_length=20)

class Physical_details(models.Model):       #done
    height=models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    blood_group=models.CharField(max_length=20)
    body_type=models.CharField(max_length=20)
    complexion = models.CharField(max_length=20)
    smoke_habbit = models.CharField(max_length=20)
    drinking_habbit = models.CharField(max_length=20)
    physical_detail_updated_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Photo_id(models.Model):
    photo_id=models.IntegerField()
    status=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=20)

class Image_gallary(models.Model):
    Customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    # image=models.ImageField(upload_to='photos',verbose_name="image")
    created_at= models.DateTimeField(auto_now_add=True)

class Profile_feedback(models.Model):
    Customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=100)
    message=models.CharField(max_length=300)
    remark=models.CharField(max_length=30)
    remark_by=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=20)

class System_feedback(models.Model):
    Customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    contact_no=models.DecimalField(max_digits=10,decimal_places=1)
    email=models.EmailField(max_length=50)
    feedback=models.CharField(max_length=300)
    remark=models.CharField(max_length=30)
    remark_by=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=30)
