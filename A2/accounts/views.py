from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseNotFound
from .forms import ProfileEdit,RegisterForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/accounts/profile/view/')
        else:
            return render(request,'accounts/login.html',{'error':'Username or Password is Invalid.'})
    return render(request,'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
@login_required
def profile_view(request):
    user = request.user
    data = {
        'id':user.id,
        'username':user.username,
        'email':user.email,
        'first_name':user.first_name,
        'last_name':user.last_name
    }
    return JsonResponse(data)
@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileEdit(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            if password1:
                user.set_password(password1)
            user.save()
            return redirect('accounts/profile/view/')
    else:
        form = ProfileEdit(instance=user)
    return render(request,'accounts/profile_edit.html',{'form':form})