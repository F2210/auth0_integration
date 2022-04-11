import json, os
import sentry_sdk, random, string
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, HttpResponse
from jose import jwt

User = get_user_model()

JWT_AUTHKEY = os.getenv('JWT_AUTHKEY')
JWT_ENCKEY = os.getenv('JWT_ENCKEY')

def randomstring(length=100):

    res = ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=length
        )
    )

    return res


def auth0Login(request):
    sentry_sdk.capture_message("jwt token found")

    jwt_key = request.GET.get("JWT")
    auth_key = request.GET.get("AUTH_KEY")

    if auth_key == JWT_AUTHKEY:

        sentry_sdk.capture_message("auth token correct")

        payload = jwt.decode(jwt_key, JWT_ENCKEY, algorithms=['HS256'])

        try:

            user = User.objects.get(pk=payload.get("id"))
            login(request, user)

        except User.DoesNotExist:

            return HttpResponse('Dit account bestaat niet.', status_code=400)

    else:
        return HttpResponse(f"AUTHKEY invalid, {auth_key}")

def auth0Users(request):

    if request.method == "POST":

        sentry_sdk.capture_message("jwt token found")

        auth_key = request.POST.get("AUTH_KEY")

        if auth_key == JWT_AUTHKEY:

            sentry_sdk.capture_message("auth token correct")

            payload = request.POST

            user = User.objects.filter(email=payload['email'])

            if user.exists():
                return HttpResponse(f"User already exists", status_code=400)

            else:
                user = User.objects.create_user(payload.get('email'), payload.get('email'), randomstring())

                return HttpResponse(json.dumps({
                    "id": user.pk,
                    "user": {
                        "email": payload["email"],
                        "name": payload["email"],
                    }
                }))

        else:
            return HttpResponse(f"AUTHKEY invalid, {auth_key}")

    elif request.method == "GET":

        jwt_key = request.GET.get("JWT")
        auth_key = request.GET.get("AUTH_KEY")

        if auth_key == JWT_AUTHKEY:

            sentry_sdk.capture_message("auth token correct")

            payload = jwt.decode(jwt_key, JWT_ENCKEY, algorithms=['HS256'])

            try:
                User.objects.get(pk=payload["id"])

            except User.DoesNotExist:
                return HttpResponse('Unauthenticated', status_code=403)

            users = User.objects.filter(email=request.GET.get("search"))

            if users.exists():

                userslist = [{"id": i.id} for i in users]

                return HttpResponse(json.dumps(userslist), status_code=200)

            else:
                return HttpResponse('Account not found', status_code=500)

        else:
            return HttpResponse(f"AUTHKEY invalid, {auth_key}")

    elif request.method == "DELETE":

        jwt_key = request.GET.get("JWT")
        auth_key = request.GET.get("AUTH_KEY")

        if auth_key == JWT_AUTHKEY:

            sentry_sdk.capture_message("auth token correct")

            payload = jwt.decode(jwt_key, JWT_ENCKEY, algorithms=['HS256'])

            try:
                user = User.objects.get(pk=payload["id"])
                user.delete()

                return HttpResponse('account removed', status_code=200)
            except User.DoesNotExist:
                return HttpResponse('Account not found', status_code=403)

        else:
            return HttpResponse(f"AUTHKEY invalid, {auth_key}")