from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    # return render(request,'appTwo/user.html')
    #
    # users_list = User.objects.order_by('first_name')
    # users_dict = {'users_records': users_list}
    # # my_dict = {'insert_content': "Hello I am from FirstApp!"}
    # return render(request,'appTwo/user.html',context=users_dict,{'form': form})
    return render(request,'appTwo/user.html',{'form': form})

def user1(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users_records': users_list}
    # my_dict = {'insert_content': "Hello I am from FirstApp!"}
    return render(request,'appTwo/user.html',context=users_dict)
