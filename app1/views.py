from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import clform, tform
from .models import cltt, tett
from django.template import RequestContext
from .calctt import func1

# Create your views here.

def handler400(request, *args, **argv):
    response = render(
        request,
        'app1/400.html',
        {
            'title': "400 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 400
    return response

def handler404(request, *args, **argv):
    response = render(
        request,
        'app1/404.html',
        {
            'title': "404 Not found",
            'year':datetime.now().year,
        }
    )
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(
        request,
        'app1/500.html',
        {
            'title': "500 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 500
    return response

def handler503(request, *args, **argv):
    response = render(
        request,
        'app1/503.html',
        {
            'title': "503 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 503
    return response


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app1/index.html',
        {
            'title': "Home Page",
            'year':datetime.now().year,
        }
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("app1:home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(
                request,
                "app1/register.html",
                {
                    'title': "Registeration Page",
                    'year': datetime.now().year,
                    'form': form
                }
            )

    form = UserCreationForm
    return render(
        request,
        "app1/register.html",
        {
            'title': "Registeration Page",
            'year': datetime.now().year,
            'form': form
        }
    )


def login_re(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request,
        "app1/login.html",
        {
            'title': "Registeration Page",
            'year': datetime.now().year,
            'form': form
        }
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("app1:home")

def cla(request):
    assert isinstance(request, HttpRequest)	
    if request.method == "POST":
        print(f"post req")
        form = clform(request.POST)
        if form.is_valid():
            cln = form.cleaned_data['clno']
            cle = form.cleaned_data['clse']
            clt = form.cleaned_data['cltime']
            if cltt.objects.filter(clno = cln).filter(clse = cle).filter(cltime = clt):
                da = cltt.objects.get(clno = cln, clse = cle, cltime = clt)
                # da = da.get(clno = cln)
                # da = da.get(clse = cle)
                # da = da.get(cltime = clt)
				# print(da.clno)
                # for d in da:
                #     print(d.clno, d.clse, d.cltime)
                    
                messages.info(request, f"You are Viewing Time table for: {cln} {cle} {clt}")
                return render(
                    request,
                    'app1/class.html',
                    {
                        'form':form,
                        'tbsh':1,
    					'data':da,
    					'year':datetime.now().year,
    				}
    			)
                
            else:
                messages.error(request, f"No Time table found for: {cln} {cle} {clt}")
                
        else:
            messages.error(request, f"Invalid Entry")
            
    form = clform()
    return render(
        request,
        'app1/class.html',
        {
    		'form':form,
    		'title':'Class Time Table',
    		'tbsh':0,
    		'year':datetime.now().year,
    	}
    )

def classes(request):
    assert isinstance(request, HttpRequest)
    da = cltt.objects.all()
    return render(
        request,
        'app1/classes.html',
        {
			'title':'All Classes',
			'datas':da,
			'year':datetime.now().year,
		}
	)


def tea(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        print(f"post req")
        form = tform(request.POST)
        if form.is_valid():
            tidi = form.cleaned_data.get('tid')
            if tett.objects.filter(tid = tidi):
                da = tett.objects.get(tid = tidi)
                func1(tidi)
                messages.info(request, f"You are Viewing Time table for teacher: {tidi}")
                # print(da.tid)
                # print(da.fname)
                return render(
                    request,
                    'app1/teacher.html',
                    {
                        'form': form,
                        'title': 'Teacher Time Table',
                        'tbsh': 1,
                        'data': da,
    					'year': datetime.now().year,
                    }
                )
            
            else:
                messages.error(request, f"No Time table found for: {tidi}")

        else:
            messages.error(request, f"Invalid Entry")

    form = tform()
    return render(
        request,
        'app1/teacher.html',
        {
    		'form':form,
    		'title':'Teacher Time Table',
    		'tbsh':0,
    		'year':datetime.now().year,
    	}
    )

def ur(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app1/user.html',
        {
            'title': 'User Page',
            'year': datetime.now().year,
        }
    )