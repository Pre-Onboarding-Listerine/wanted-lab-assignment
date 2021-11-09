import json

from django.http      import JsonResponse
from django.views     import View

from .models      import Company, CompanyName, Tag

class CompanyDetailView(View):
    def get(self, request, keyword):
        try:
            language = request.headers.get('x-wanted-language')
            companyname = CompanyName.objects.get(name=keyword)
            
            user_company_name = CompanyName.objects.get(company_id=companyname.company.id,lang=language)

            company_info ={
                'company_name' : user_company_name.name,
                'tags' : [tag.name for tag in companyname.company.tags.all() if tag.lang ==language]
            }

            return JsonResponse({'message': company_info}, status=200)

        except CompanyName.DoesNotExist:
            return JsonResponse({'message': 'Does_Not_Exist_Error'}, status=404)
