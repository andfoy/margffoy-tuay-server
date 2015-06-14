import redis
from django.shortcuts import render
from django.http import HttpResponse

def home_chat(request):
    #csrf_token = csrf(request)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    user = request.user
    username = 'Someone'
    if user.is_authenticated():
       username = user.username
    r.set('user', username)
    return render(request, 'chat/index.html', locals())

def process_message(request):
    if request.method == 'POST':
       r = redis.StrictRedis(host='localhost', port=6379, db=0)
       r.set('msg', 'Trying...')
       user = request.user
       username = 'Someone'
       if user.is_authenticated():
          username = user.username
       msg = request.POST.get('msg')
       data = '%s : %s' % (username, msg)
       r.publish('chat-channel', data)
       #r.set('msg', data)
       return HttpResponse("200 OK")
    else:
       return HttpResponse("Not Allowed")

def user_leave(request):
    if request.method == 'POST':
       r = redis.StrictRedis(host='localhost', port=6379, db=0)
       user = request.user
       username = 'Someone'
       if user.is_authenticated():
          username = user.username
       r.set('user_logout', username)
       #r.set('msg', data)
       return HttpResponse("200 OK")
    else:
       return HttpResponse("Not Allowed")


