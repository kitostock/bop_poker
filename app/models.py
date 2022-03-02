from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


class Task(models.Model):

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


    
class MenberInfoModel(models.Model):
    user_id = models.CharField(max_length=11, primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_paid_member = models.BooleanField(default=False)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_id

class BopInfoModel(models.Model):
    user_id = models.CharField(max_length=11)
    category_id = models.CharField(max_length=255)
    buy_in = models.CharField(max_length=255)
    cash_out = models.IntegerField(max_length=255)
    number_of_hands = models.IntegerField(max_length=255)
    register_date = models.DateTimeField(blank=True, null=True)
    memo = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_id

class PersonalCategoryModel(models.Model):
    category_id = models.CharField(max_length=11)
    user_id = models.CharField(max_length=11)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_id
# BopInfoレスポンス　category_id　basecategory１キャッシュ　basecategory2 トーナメントでAPIでマッピング　
# それ以外はいずれアディショナルカテゴリインフォ検索し返却

class PersonalRateModel(models.Model):
    rate_id = models.CharField(max_length=11)
    user_id = models.CharField(max_length=11)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.rate_id

# Create your models here.
class ItemCategoryModel(models.Model):
    item_category_name = models.CharField(max_length=255)
 
    def __str__(self):
        return self.item_category_name
    
class ItemModel(models.Model):
    item_name = models.CharField(max_length=255)
    item_category_id = models.ForeignKey(
        ItemCategoryModel,
        on_delete=models.CASCADE)
 
    def __str__(self):
        return self.item_name