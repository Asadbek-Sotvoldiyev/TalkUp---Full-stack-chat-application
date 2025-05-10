from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")
    

class UpdateProfileView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            country = data.get("country")
            region = data.get("region")
            gender = data.get("gender")
            bio = data.get("bio")

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.country = country
            request.user.city = region  
            request.user.gender = gender
            request.user.bio = bio
            request.user.save()
            return JsonResponse({"message": "Profile updated successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)


class UpdateProfilePhotoView(View):
    def post(self, request, *args, **kwargs):
        photo = request.FILES.get('photo')

        if not photo:
            return JsonResponse({'status': 'error', 'message': 'No photo uploaded'}, status=400)

        user = request.user
        user.photo_url = photo
        user.save()

        return JsonResponse({
            'status': 'success',
            'photo_url': user.photo_url.url,
            "message": "Photo updated successfully"
        })


def logout_user(request):
    logout(request)
    messages.warning(request, "You have been logged out")
    return redirect('home')

