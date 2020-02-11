from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from profiles.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Category, Add_Products, Post_advertise
import datetime
from .forms import AddproductForm, AddadvertiseForm
# Create your views here.


@login_required
def deshboard(request):

	return render(request, 'dealer/index.html')

@login_required
def addcategory(request):
	display = Category.objects.filter(created_by=request.user)
	if request.method == 'POST' and request.FILES['category_image'] :
		cat_image = request.FILES['category_image']
		fs = FileSystemStorage()
		file_name = fs.save(cat_image.name, cat_image)
		

		#uploded_file_url = fs.url(category_imag0e)
		cat_name=request.POST['name']
		cat_des = request.POST['cat_descryption']
		
		Category.objects.create(category_name = cat_name, category_describe = cat_des, category_image = file_name,created_by=request.user)
		
		#all_cat = Category.objects.all()
    
		return render(request, 'dealer/index.html',{'all_cat':display})
        

	else:
		return render(request, 'dealer/addcategory.html',{'all_cat':display})



def addproduct(request):
	# show = Product.objects.all()
	data = Add_Products.objects.filter(creaed_by = request.user)
	if request.method == 'POST':
		
		form= AddproductForm(request.POST,request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.creaed_by = request.user
			form.save()


			return redirect('deshboard')
		# file_name = fs.save(product_image.name, product_image)
	
	

	else:
			form = AddproductForm()
	return render(request, 'dealer/addproduct.html',{'form':form,'data':data})

		


def addad(request):
	data = Post_advertise.objects.filter(product_by=request.user)
	if request.method=='POST':
		form = AddadvertiseForm(request.POST)
		if form.is_valid():
			form=form.save(commit=False)
			form.product_by=request.user
			form.save()
			return redirect('deshboard')
	else:
		form = AddadvertiseForm()
	return render(request,'dealer/addadvertise.html',{'form':form,'data':data})

# this is for farmer show ad

