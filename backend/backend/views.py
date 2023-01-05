from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . import models

@csrf_exempt
def login(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if models.authenticate(username = data.get("username"), password= data.get("password") ):
			return JsonResponse({"result": True})
		else:
			return JsonResponse({"result": False})
		# POST request
	else:
		# Method Not Allowed
		return HttpResponse("method not allowed")


# Great 

def create(request):
	if request.method == "POST":
		data = json.loads(request.body)
		user_name = data.get("username")
		password = data.get("auth_password")
		models.create_user(username=user_name,password=password)

	else:
		return HttpResponse("method not allowed")


def admin(request):
	admin_name = "ISHAAN"
	password_admin = "afkaj()jhhkbvhdu87 tiyfhv"
	if request.method == "POST":
		data = json.loads(request.body)
		username = data.get("adminname")
		password= data.get("password")
		if username == admin_name and password == password_admin:
			data = json.loads(models.give_all())
			return JsonResponse(data)

	else: return HttpResponse("sorry!!")		



def home(request):
  	return JsonResponse({"result": False})