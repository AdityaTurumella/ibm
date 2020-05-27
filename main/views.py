from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def video(request):

    return render(request,'main/video.html')


def home(request):
	return render(request, 'main/home.html')


def register ( request ) :
    if request.method == "POST" :
        form = NewUserForm( request.POST )
        if form.is_valid( ) :
            user = form.save( )
            username = form.cleaned_data.get( 'username' )
            c = str( {username} )
            messages.success( request , "New account created " + username )
            login( request , user )
            return redirect( "main:home" )
        else :
            for msg in form.error_messages :
                c = str( {form.error_messages[msg]} )
                messages.error( request , c )
                return render( request = request ,
                               template_name = "main/register.html" ,
                               context = {"form" : form} )

    form = NewUserForm
    return render( request = request ,
                   template_name = "main/register.html" ,
                   context = {"form" : form} )


def logout_request ( request ) :
    logout( request )
    messages.info( request , 'logout successful' )
    return redirect( 'main:home' )


def login_request ( request ) :
    form = AuthenticationForm( )
    return render( request , 'main/login.html' , {'form' : form} )


def login_request ( request ) :
    if request.method == 'POST' :
        form = AuthenticationForm( request = request , data = request.POST )
        if form.is_valid( ) :
            username = form.cleaned_data.get( 'username' )
            password = form.cleaned_data.get( 'password' )
            user = authenticate( username = username , password = password )
            if user is not None :
                login( request , user )
                messages.info( request , "You are now logged in as " + username )
                return redirect( '/' )
            else :
                messages.error( request , "Invalid username or password." )
        else :
            messages.error( request , "Invalid username or password." )
    form = AuthenticationForm( )
    return render( request = request ,
                   template_name = "main/login.html" ,
                   context = {"form" : form} )



def about(request):
    return render(request,'main/about.html')

