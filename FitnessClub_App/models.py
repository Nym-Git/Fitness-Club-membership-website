from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User



# card models...
class TrainingSlotCard(models.Model):
  Trainee_Name = models.ForeignKey(User, on_delete=models.CASCADE)
  Category = models.CharField(max_length=50,null=True)
  Heading = models.CharField(max_length=33)
  Training_period = models.CharField(max_length=30,blank=True)
  Image = models.FileField(blank=True, upload_to='Cards/')
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Heading


class Category(models.Model):
  Category_Field = models.CharField(max_length=200,null=True)
  Image = models.FileField(blank=True, upload_to='Icons/')
  published_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.Category_Field


class TrainingCardDetail(models.Model):
  Trainer_play = models.ForeignKey(TrainingSlotCard, on_delete=models.CASCADE, default=0)
  Trainer_Name = models.CharField(max_length=33, default="null")
  Video = models.FileField(blank=True, upload_to='Videos/')
  Seven_Day_Rate = models.IntegerField(default=0)
  One_Month_Rate = models.IntegerField(default=0)
  Three_Months_Rate = models.IntegerField(default=0)
  One_year_Rate = models.IntegerField(default=0)
  Two_year_Rate = models.IntegerField(default=0)
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Trainer_Name


class UserAccount(models.Model):
  User_Name = models.CharField(max_length=33, blank=False)
  First_Name = models.CharField(max_length=100, blank=False)
  Last_Name = models.CharField(max_length=100, blank=False)
  Image = models.FileField(blank=True, upload_to='UserProfileImage/', default='Icons/dp.jfif')
  about = models.CharField(max_length=800, blank=True)
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.User_Name



class UsersPaymentHistory(models.Model):
  Trainer_Name = models.CharField(max_length=33, blank=False)
  User_Name = models.CharField(max_length=33, blank=False)
  Trainer_play = models.ForeignKey(TrainingSlotCard, on_delete=models.CASCADE)
  imageURL = models.CharField(max_length=3300, default='null')
  active = models.BooleanField(default=False)
  expire_date = models.CharField(max_length=330, blank=False)
  Buying_date = models.DateTimeField(default=timezone.now)
  CardId = models.CharField(max_length=33, default="null") 

  def __str__(self):
    return self.User_Name


class UploadClassVideos(models.Model):
  Trainer= models.CharField(max_length=100) 
  Trainer_play = models.CharField(max_length=100) 
  f_name = models.CharField(max_length=255, blank=True, default='NULL')
  myfiles = models.FileField(upload_to="ClassVideos")
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Trainer_play