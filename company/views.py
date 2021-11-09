from django.shortcuts import render

# Create your views here.
from .models import CompanyName
from django.http import JsonResponse
from rest_framework.views import APIView
import json


class SearchView(APIView):
	def get(self, request):
		try:
			word = request.GET.get('query', '')
			results=[]

			companies  = CompanyName.objects.filter(name__icontains = word)
			
			if not companies:
				return JsonResponse({[
		        {"company_name": "wecode_wanted"},
        {"company_name": "wecode"}]},status=200)
			
			for company in companies:
				results.append({"company_name": company.name})			
			return JsonResponse({"data": results}, status=200)
		
		except Exception as error:
			return JsonResponse({'message': '서버가 이상합니다.'}, status=500)
