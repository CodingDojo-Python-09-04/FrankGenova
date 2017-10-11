from django.http import HttpResponse

def hello_world(request):
    print('hello world')
    message = 'Hello World'
    return HttpResponse(message)

def alt_view(request):
    print('in alt_view')
    message = 'Alt View'
    return HttpResponse(message)