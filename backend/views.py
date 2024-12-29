import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from backend.models import User

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        username = request.GET.get('username', '').strip()
        gender = request.GET.get('gender', '').strip().upper()

        # if not username or gender not in ['M', 'F', 'O']: # ! fix this later
        #     raise ValidationError('Invalid input: username or gender.') 

        user = User(username=username, gender=gender)
        user.save()

        response['respMsg'] = 'success'
        response['respCode'] = '000000'
    except ValidationError as e:
        response['respMsg'] = str(e)
        response['respCode'] = '400001'
    except IntegrityError as e:
        response['respMsg'] = 'Username already exists.'
        response['respCode'] = '400002'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_users(request):
    response = {}
    try:
        users = User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['respMsg'] = 'success'
        response['respCode'] = '000000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)

# ! TODO: disable csrf. this is dangerous, fix it when deployment
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_all_users(request):
    response = {}
    try:
        # 删除所有的用户
        User.objects.all().delete()
        
        response['respMsg'] = 'All users deleted successfully'
        response['respCode'] = '000000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    
    return JsonResponse(response)