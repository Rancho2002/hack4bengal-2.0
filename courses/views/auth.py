from django.shortcuts import render , redirect
from django.contrib.auth import logout , login, authenticate
from courses.forms import RegistrationForm , LoginForm
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

def signup(request):
    print(request.POST)
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        return redirect('login')
    return render(request, 'courses/signup.html')
    
def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'courses/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'courses/login.html', {'error': 'Invalid username or password.'})

# @require_http_methods(['GET', 'POST'])
# def login_view(request):
#     template_name = "courses/login.html"
#     form = LoginForm(request.POST or None)
#     next_page = request.GET.get('next')

    
#     if request.method=="POST":
#         email=request.post.get("email")
#         password=request.post.get("password")
        
#     if form.is_valid():
#         login(request, form.cleaned_data)
#         if next_page is not None:
#             return redirect(next_page)
#         return redirect('/')

#     context = {
#         'form': form,
#     }
#     return render(request, template_name, context)



def signout(request ):
    logout(request)
    return redirect("home")

