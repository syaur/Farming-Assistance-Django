from django.db import models
from django.conf import settings
from profiles.models import User

# Create your models here.


class Category(models.Model):

	category_name = models.CharField(max_length = 50)

	category_describe = models.TextField(null=True)
	
	category_image = models.ImageField(upload_to = 'category-images/',null=True)

	created_by = models.ForeignKey(User, related_name="Users", on_delete = models.CASCADE)

	created_at = models.DateField(auto_now = True)

	updated_at = models.DateField(auto_now_add = True, null = True, blank = True)

	def __str__(self):
		return '%s' %(self.category_name)


class Add_Products(models.Model):
    product_name = models.CharField(max_length = 50)

    brand_name = models.CharField(max_length = 30)

    product_desc = models.TextField()

    size = models.IntegerField()

    price = models.IntegerField()

    product_image = models.ImageField(upload_to = 'product-images/')

    product_type = models.CharField(max_length = 60, null = True)

    category_name = models.ForeignKey(Category, related_name="Categorys", on_delete = models.CASCADE)

    creaed_by = models.ForeignKey(User, related_name="User", on_delete = models.CASCADE, null = True)

    def __str__(self):
    	return '%s' %(self.brand_name)


class Post_advertise(models.Model):
	product_name = models.ForeignKey(Add_Products, related_name = 'Post_advertise', on_delete = models.CASCADE)

	category_name = models.ForeignKey(Category, related_name = 'Post_advertise', on_delete = models.CASCADE, null = True)

	# = models.ForeignKey(User, related_name = 'Post_advertise', on_delete = models.CASCADE)

	product_by = models.ForeignKey(User, related_name = "Usr", on_delete=models.CASCADE,null = True)

	
	def __str__(self):
		return '%s' %(self.product_type)


