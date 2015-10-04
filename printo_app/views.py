from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Document, Organization, UserProfile, Shop
<<<<<<< HEAD
from .forms import DocUploadForm, ShopEditForm, ShopCreateForm, UserForm
from django.template import RequestContext


def custom_proc(request):
    # "A context processor that provides 'app', 'user' and 'ip_address'."
    user = UserProfile.objects.get(user=request.user)
    return {
        'user': request.user,
        'user_role': user.get_userType_display()
    }

# Create your views here.
def index(request):
	user = UserProfile.objects.get(user=request.user)
	if(user.userType == 1):
		return HttpResponseRedirect(reverse('OwnerMain'))
	elif(user.userType == 2):
		return HttpResponseRedirect(reverse('EmployeeMain'))
	return None

def indexEmp(request,shopid=None):
	user = UserProfile.objects.get(user=request.user)
	is_owner = False
	if(user.userType == 1):
		is_owner = True
	elif(user.userType == 2):
		is_owner = False
	context = {'is_owner':is_owner}
	return HttpResponseRedirect(reverse('ordersList'))

def ordersList(request,shopid=None):
	context = {}
	return render(request,'printo_app/ordersList.html',context,context_instance=RequestContext(request, processors=[custom_proc]))

def docUploadOwner(request):
	user = UserProfile.objects.get(user=request.user)
	if(request.method=='POST'):
		
		org = Organization.objects.get(owner = request.user)
		
		data = DocUploadForm(request.POST,request.FILES)

		new_doc = data.save(commit=False)
		new_doc.organization = org
		new_doc.is_public = True
		new_doc.save()
		data.save_m2m() 
		return HttpResponseRedirect(reverse('documentList'))
	else:
		form = DocUploadForm()
		context = { "docUploadForm" : form }
		
		return render(request,'printo_app/docUpload-owner.html',context,context_instance=RequestContext(request, processors=[custom_proc]))
	return None	

def docUpload(request):
	user = UserProfile.objects.get(user=request.user)
	if(request.method=='POST'):
		
		
		org = Organization.objects.get(employee = request.user)
=======
from .forms import DocUploadForm, ShopEditForm


# Create your views here.

def indexEmp(request):
	context = {'shop':shopid}
	return render(request,'index.html',context)

def docUpload(request):
	if(request.method=='POST'):
		user = UserProfile.objects.get(user=request.user)
		if(user.userType == 1 ):
			org = Organization.objects.get(owner = request.user)
		elif(user.userType == 2):
			org = Organization.objects.get(employee = request.user)
>>>>>>> origin/master
		# import ipdb;ipdb.set_trace();
		data = DocUploadForm(request.POST,request.FILES)

		new_doc = data.save(commit=False)
		new_doc.organization = org
		new_doc.is_public = True
		new_doc.save()
		data.save_m2m() 
		return HttpResponseRedirect(reverse('documentList'))
	else:
		form = DocUploadForm()
		context = { "docUploadForm" : form }
<<<<<<< HEAD
		
		return render(request,'printo_app/docUpload.html',context,context_instance=RequestContext(request, processors=[custom_proc]))
	return None

def docListOwner(request):
	user = UserProfile.objects.get(user=request.user)		
	org = Organization.objects.get(owner = request.user)
	docList = Document.objects.filter(is_public=True).filter(organization=org)
	context = {"docs":docList}
	return render(request,'printo_app/docList-owner.html',context,context_instance=RequestContext(request, processors=[custom_proc]))


def docList(request):
	user = UserProfile.objects.get(user=request.user)		
	org = Organization.objects.get(employee = request.user)
	docList = Document.objects.filter(is_public=True).filter(organization=org)
	context = {"docs":docList}
	return render(request,'printo_app/docList.html',context,context_instance=RequestContext(request, processors=[custom_proc]))
=======
		return render(request,'printo_app/docUpload.html',context)

def docList(request):
	user = UserProfile.objects.get(user=request.user)
	if(user.userType == 1  ):
		org = Organization.objects.get(owner = request.user)
	elif(user.userType == 2):
		org = Organization.objects.get(employee = request.user)
	docList = Document.objects.filter(is_public=True).filter(organization=org)
	context = {"docs":docList}
	return render(request,'printo_app/docList.html',context)
>>>>>>> origin/master

def docDetail(request,docid):
	docDetail = Document.objects.get(id=docid)
	form = DocUploadForm(instance = docDetail)
	context = {"docEditForm":form,"doc":docDetail}
<<<<<<< HEAD
	return render(request,'printo_app/docDetail.html',context,context_instance=RequestContext(request, processors=[custom_proc]))
=======
	return render(request,'printo_app/docDetail.html',context)
>>>>>>> origin/master

def docEditSave(request,docid):
	# import ipdb;ipdb.set_trace();
	currentDoc = Document.objects.get(id=docid)
	docDetail = DocUploadForm(request.POST,request.FILES,instance=currentDoc)
	docDetail.save()	
	context = { "msg":docDetail }
	return HttpResponseRedirect(reverse('documentList'))

<<<<<<< HEAD
def shopList(request):
	org = Organization.objects.get(owner = request.user)
	shops = Shop.objects.filter(owner = org )
	context={'shops' : shops}
	return render(request,'printo_app/shopList.html',context)

def shopCreate(request):
	# import ipdb; ipdb.set_trace()
	if(request.method=='POST'):
		userform = UserForm(request.POST,prefix='user')
		shopform = ShopCreateForm(request.POST,prefix='shopProfile')
		
		if(userform.is_valid):
			user = userform.save()
			userprofile = UserProfile()
			userprofile.user = user
			userprofile.userType = 2
			userprofile.save()
			shopprofile = shopform.save(commit=False)
			shopprofile.employee = user
			shopprofile.owner = Organization.objects.get(owner = request.user)
			shopprofile.save()
			shopform.save_m2m()

			return HttpResponseRedirect(reverse('shopList'))
	else:
		userform = UserForm(prefix='user')
		shopform = ShopCreateForm(initial={'owner': Organization.objects.get(owner = request.user)},prefix='shopProfile')
		context = { 'shopCreateForm' : shopform, 'userForm' : userform }
	return render(request,'printo_app/shopCreate.html',context)

=======
>>>>>>> origin/master
def shopProfile(request,shopid=None):
	# import ipdb; ipdb.set_trace()
	context = {}
	user = UserProfile.objects.get(user=request.user)
	if(user.userType == 1):
<<<<<<< HEAD
		pass
=======
		import ipdb; ipdb.set_trace()
>>>>>>> origin/master
	elif(user.userType == 2):
		shop = Shop.objects.get(employee=request.user)
		shopForm = ShopEditForm(instance=shop)
	context = {'shopForm':shopForm}
<<<<<<< HEAD
	return render(request,'printo_app/shopProfile.html',context,context_instance=RequestContext(request, processors=[custom_proc]))
=======
	return render(request,'printo_app/shopProfile.html',context)
>>>>>>> origin/master

def shopEditSave(request):
	shop = Shop.objects.get(employee=request.user)
	shopForm = ShopEditForm(request.POST,instance=shop)
	shopForm.save()
	return HttpResponseRedirect(reverse('shopProfile'))

<<<<<<< HEAD
def indexOwner(request):
	context = {}
	return render(request,'ownerMain.html',context)


=======
# def indexOwner(request)//
>>>>>>> origin/master

