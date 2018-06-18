from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
import json
from datetime import datetime, timedelta
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def index(request):
    users = list(User.objects.all())[0].as_json()
    resp = JsonResponse(users)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp 

@csrf_exempt 
def userRegister(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        print(post_data)

        try:
            user = User.objects.create(Username= post_data['Username'], Password= post_data['Password'], Email= post_data['Email'], Firstname= post_data['Firstname'], Lastname= post_data['Lastname'])
            user.save()
        except:
            return JsonResponse({
                'status': 'fail',
                'data': {
                    'message': 'There is an error during add new user to database'
                }
            }, status=500)


        res = JsonResponse({
            'status': 'success',
            'data': str(post_data)
        })
        res['Access-Control-Allow-Origin'] = '*'
        res.set_cookie('token', value='', expires=datetime.utcnow() + timedelta(days=30))
        return res
    else:
        return render(request, 'userRegister.html')

def authenticate(username, password):
    user = User.objects.get(Username=username)
    if user.Password == password:
        return True
    else:
        return False

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        print(post_data)
        if authenticate(post_data['Username'], post_data['Password']):
            user = User.objects.get(Username = post_data['Username'])
            rt = {
                'Username': user.Username,
                'Password': user.Password,
                'Email': user.Email,
                'Firstname': user.Firstname,
                'Lastname':  user.Lastname
            }
            res = JsonResponse({
                'status': 'success',
                'data': rt
            })
            res['Access-Control-Allow-Origin'] = '*'
            res.set_cookie('token', value='', expires=datetime.utcnow() + timedelta(days=30))
            return res
        else:
            return JsonResponse({
                'status': 'fail',
                'data': {
                    'message': 'The password do not match the username'
                }
            }, status=401)

    else:
        return render(request, 'login.html')


    



    

