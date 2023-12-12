from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponse
from .models import Instruction
from django.contrib.auth.decorators import login_required

@login_required(login_url='main/login.html')
def homepage(request):
    return render(request, 'main/homepage.html')

def logout(request):
    if request == 'POST':
        logout = request.POST.get('logout')

    return render(request, 'main/login.html')



def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Set user ID and username in the session
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            return redirect('homepage')
        else:
            return HttpResponse("Username or password incorrect!")

    return render(request, 'main/login.html')




from django.shortcuts import render
from .models import Instruction  # Assuming your model is imported from a module named models

@login_required(login_url='main/login.html')
def home(request):
    # Check if the form is submitted with the 'locate' action
    if request.method == 'POST':

        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        if origin and destination:
            instructions = Instruction.objects.filter(origin=origin, destination=destination)
            return render(request, 'main/homepage.html', {'instructions': instructions})


    # Render the initial form or page
    return render(request, 'main/homepage.html', {'instructions': None})





def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            error_message = "Passwords do not match."
            return render(request, 'main/signup.html', {'error': error_message})

        my_user = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
        my_user.save()

        return redirect('login')

    return render(request, 'main/signup.html')



from .models import Instruction

def share_view(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        instruction_text = request.POST.get('instruction')
        
        # Assuming you have the user stored in the session with key 'user_id'
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        
        # Create and save the Instruction object
        instruction = Instruction.objects.create(
            origin=origin,
            destination=destination,
            instruction=instruction_text,
            user=user
        )
        
        # Redirect to a success page or any other desired page
        return redirect('homepage')

    return render(request, 'main/share.html')

def accounts (request):

    return render(request, 'main/accounts.html')

def contacts(request):

    return render(request, 'main/contacts.html')

def aboutus (request):
    return render(request,  'main/about.html')