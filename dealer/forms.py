from django import forms
from .models import Category, Add_Products, Post_advertise


class AddproductForm(forms.ModelForm):
	class Meta:
		model = Add_Products
		fields = ('product_name','brand_name','product_desc','product_image','size','price','product_type','category_name')
		
	


class AddadvertiseForm(forms.ModelForm):
	class Meta:
		model = Post_advertise
		fields = ('__all__')
		exclue = ('product_by')
