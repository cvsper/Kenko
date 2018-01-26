from django.http import JsonResponse
from kenkoapp.models import Carepro
from kenkoapp.serializers import CareproSerializer

def customer_get_carepro(request):
	carepro = CareproSerializer(
		Carepro.objects.all().order_by('-id'),
		many = True
		).data
	return JsonResponse({'carepro' : carepro})

def customer_get_(request):

	return JsonResponse({ '' : })

def customer_get_(request):

	return JsonResponse({ '' : })	

def customer_get_(request):

	return JsonResponse({ '' : })			