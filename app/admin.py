from django.contrib import admin

from .models import (Task, Post, BopInfoModel, PersonalCategoryModel, ItemCategoryModel, ItemModel,
                     MenberInfoModel, PersonalRateModel)

# Register your models here.
admin.site.register(Post)
admin.site.register(Task)

admin.site.register(ItemCategoryModel)
admin.site.register(ItemModel)
admin.site.register(MenberInfoModel)
admin.site.register(BopInfoModel)
admin.site.register(PersonalCategoryModel)
admin.site.register(PersonalRateModel)
