from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import models

# Create your views here.

def home(request):
    profil = models.Profile.objects.get(user__id= request.user.id)
    profils = models.Profile.objects.filter()

    data = {
        'profil': profil, 
        'profils': profils,
    }
    return render(request, "pages/index.html", data)



def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('******************************************************', username, password )
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, "pages/login.html")



def inscription(request):
    if request.method == "POST" :
        success = False
        username = request.POST.get('username')
        image = request.FILES.get('image')
        contact = request.POST.get('contact')
        lien_fb = request.POST.get('lien_fb')
        lien_twt = request.POST.get('lien_twt')
        lien_insta = request.POST.get('lien_insta')
        password = request.POST.get('password')

        print(username, image, lien_fb, contact, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        
        if username is not None and image is not None and contact is not None : 
            user = User(
                username=username,
            )
            try :
                user.save()
                print(user, '*******************************************')
                print('************************* succes ***********************************')
                user.profileUser.image=image
                user.profileUser.contact=contact
                user.profileUser.lien_fb=lien_fb
                user.profileUser.lien_twt=lien_twt
                user.profileUser.lien_insta=lien_insta
                user.profileUser.save()
                user.password=password
                user.set_password(user.password)
                user.save()
                print('************************* succes ***********************************')
                success = True
                response = "votre inscription a ete effectuée avec succes"
                return redirect('login')
            except Exception as e:
                print(e)
                success = False
                response = " error, veillez verifier votre connexion "
    return render(request, "pages/register.html")



        