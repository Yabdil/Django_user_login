from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

def verifying_username(objs, field):
    rend = False
    for obj in objs:
        if  str(obj) == field:
             rend = True
    return rend

def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        list_users = User.objects.all()
        existing_username = verifying_username(list_users, username)

        if password == password1:
            if User.objects.filter(username=username).exists():
            #if not existing_username
                print('this is the result')
                messages.info(request, 'Username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=firstname, username=username, email=email, password=password, last_name=lastname)
                user.save()
                return redirect('login')
                    
        else:
            return HttpResponse('Wrong Post request')

    else:
        return render(request, 'register.html')



def login(request):

    if request.method == 'POST':
        user_name = request.POST['username']
        mdp = request.POST['mdp']
        user = auth.authenticate(username=user_name, password=mdp)
        if user is not None:
            auth.login(request, user)
            return redirect('/tral')
        else:
            return redirect('login')
            
    else:
        return render(request, 'login.html')




def logout(request):

    auth.logout(request)
    return redirect('login')



def changepassword(request):
    if request.method == 'POST':
        send_email = request.POST['email_password']
        filter_email = User.objects.filter(email=send_email)
        if filter_email:
            return render(request, 'changepassword.htm')
        else:
            print('this email is not know', send_email)
            return render(request, 'changepassword.htm')
        

    return render(request, 'changepassword.htm')


    





    

