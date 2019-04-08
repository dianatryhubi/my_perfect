from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog_news, Category, Information 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.
def show_home_page(request):
	return render(request, 'mainapp/home.html', 
					{'News': Blog_news.objects.all().order_by("-id")[:3]})

def show_categories(request):
	return render(request, 'mainapp/categories.html',
					{'cat':Category.objects.all().order_by("-id")})

def separator(request, url_sl):
	categor_urls = [c.urls_slung_category for c in Category.objects.all()]
	for posts in categor_urls:
		if url_sl == posts:
			return render(request, 
					"mainapp/home.html",
					{'News':Information.objects.filter(news_catagory__urls_slung_category=url_sl)})


def show_register(request):
	if request.method=="POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			username = form.cleaned_data["username"]
			messages.success(request, f"Ви ввійшли як {username}")
			return redirect("mainapp:home")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")

	form = NewUserForm
	return render(request, 'mainapp/register.html', {"form":form})

def logout_(request):
	logout(request)
	messages.info(request, "Ви вийшли зі свого аккаунту!")
	return redirect("mainapp:home")

def login_(request):

	if request.method=="POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Ви ввійшли як {username}")
				return redirect("mainapp:home")
			else:
				messages.info(request, "Невірний пароль або логін")
		else:
			messages.error(request, f"Невірно введений пароль або логін")
	form = AuthenticationForm
	return render(request, 'mainapp/login.html', {"form":form})


def show_articul(request, id_):
	n = Blog_news.objects.get(pk=id_) 
	return render(request, 'mainapp/articul.html', {"n":n})



def show_contact(request):
	return HttpResponse("""<h1>Contacts </h1>
							Mob: +38096...""")



def show_information(request, arg):
	return HttpResponse("""<h1>Hello everyone</h1>
							My name is %s """%arg)
