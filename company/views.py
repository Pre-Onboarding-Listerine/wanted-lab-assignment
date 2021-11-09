import json

from django.http      import JsonResponse
from django.views     import View

from .models      import Company, CompanyName, Tag

class CompanyDetailView(View):
    def get(self, request):
        try:
            keyword = request.GET.get('keyword', None)

            companyname = CompanyName.objects.get(name=keyword)
            
            company_info ={
                'company_name' : companyname.name,
                'tags' : [tag.name for tag in companyname.company.tags.all()]
            }

            return JsonResponse({'message': company_info}, status=200)

        except CompanyName.DoesNotExist:
            return JsonResponse({'message': 'Does_Not_Exist_Error'}, status=404)
