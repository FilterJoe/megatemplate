#from django.template import Context, loader
#from django.http import HttpResponse
from datetime import datetime
from django.template import RequestContext # to get my css file to be seen
from django.shortcuts import render_to_response, get_object_or_404

#def hello_view(request):
#    """ Simple Hello World View """
#    t = loader.get_template('helloworld.html')
#    c = Context({
#        'current_time': datetime.now(),
#        })
#    return HttpResponse(t.render(c))
#

def hello_view(request):
    # The commented out code is here because manage.py createsuperuser quit working for me. I was
    # not able to figure out why, but to create first superuser, just uncomment the lines below.
    # Then you can log in and create another user/pwd (make superuser) and delete this first one.
#    from django.contrib.auth.models import User
#    u, created = User.objects.get_or_create(username='test3')
#    if created:
#        u.set_password('test3')
#        u.is_superuser = True
#        u.is_staff = True
#        u.save()
#        print "yeah! created test3 user!"
#    else:
#        "rats, test3 NOT created"
    current_time = datetime.now()
    return render_to_response('helloworld.html', locals(), context_instance=RequestContext(request))

def buttons_view(request):
    return render_to_response('buttons.html', locals(), context_instance=RequestContext(request))

def tabs_view(request):
    return render_to_response('tabs.html', locals(), context_instance=RequestContext(request))

def home_view(request):
    current_time = datetime.now()
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))