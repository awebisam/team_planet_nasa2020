from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact, Profile
from django.core.mail import send_mail
# Create your views here.
from .models import Newsletter


def index(request):
    return render(request, 'core/index.html',)


def team(request):
    return render(request, 'core/team.html',)


def portal(request):
    try:
        if request.user.profile:
            return render(request, 'portal/index.html',)
    except:
        return HttpResponseRedirect('accounts/profile')


def profileview(request):
    try:
        if request.user.profile:
            return HttpResponseRedirect('/portal')
    except:
        if request.method == 'POST':
            user_id, fname, lname, age = request.POST.get('user'), request.POST.get(
                'fname'), request.POST.get('lname'), request.POST.get('age')

            form = Profile(user=request.user, fname=fname,
                           lname=lname, age=age, no_of_times=1)
            form.save()
            return HttpResponseRedirect('/portal')
        else:
            return render(request, 'core/profile.html',)


def contact(request):
    if request.method == 'POST':
        fname, lname, email, message = request.POST['fname'], request.POST[
            'lname'], request.POST['email'], request.POST['message']
        contact = Contact(fname=fname, lname=lname,
                          email=email, message=message)
        contact.save()
        send_mail(
            'A new inquiry on Team Planet',
            f'''
                Enquiry by - {fname} {lname}.
                Email - {email}.
                Message: {message}.
            ''',
            'teamplanet.nasa2020@gmail.com',
            ['neetesa@gmail.com', 'henokb2124@gmail.com', 'hello@awebisam.com',
                'tiaagrawal500@gmail.com', 'shekhar.infinity@gmail.com'],
            fail_silently=False
        )
        HttpResponseRedirect('/contact')

    return render(request, 'core/contact.html')


def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form = Newsletter(email=email)
        form.save()
        send_mail(
            'Thank You',
            f'''
            Hey, {email}, we are really grateful to see you subscribing our newsletter.
            We are working on our project and will be updating about the situations with you.

            -Team Planet(Nasa Space Apps 2020)
            ''',
            'teamplanet.nasa2020@gmail.com',
            [email, ],
            fail_silently=False
        )
        return render(request, 'core/newsletter.html', {'email': email})
    else:
        return HttpResponseRedirect('/')
