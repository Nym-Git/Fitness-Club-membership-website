from django.contrib import admin
from .models import TrainingSlotCard, Category, TrainingCardDetail, UserAccount, UsersPaymentHistory, UploadClassVideos

admin.site.register(TrainingSlotCard)
admin.site.register(Category)
admin.site.register(TrainingCardDetail)
admin.site.register(UserAccount)
admin.site.register(UsersPaymentHistory)
admin.site.register(UploadClassVideos)
