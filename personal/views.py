from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
	context = {}
	# context['debug_mode'] = settings.DEBUG
	# context['debug'] = DEBUG
	# context['room_id'] = "1"
	return render(request, "personal/home.html", context)