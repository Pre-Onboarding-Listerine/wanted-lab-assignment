import json

from django.views import View
from django.http import JsonResponse
from company.models import Tag, Company

class CompanyCreateView(View):

    def post(self, request):
        try:

            language = request.headers.get("HTTP_x-wanted-language", "ko")
            print(language)
            print(type(language))

            data = json.loads(request.body)
            company_name = data["company_name"]
            tag_name = data["tags"]

            company_queryset = Company.objects.filter(company_name = company_name)
            if company_queryset.exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED COMPANY NAME'}, status = 400)               

            company = Company.objects.create(company_name = company_name)
            
            tag = Tag.objects.create(
                tag_name   = tag_name,
                company_id = company.id
            )

            result = {
                "company_name" : company.company_name[f"{language}"],
                "tags"         : []
            }

            tag_list = tag.tag_name          

            for i in range(len(tag_list)):
                result["tags"].append(
                    tag_list[i]['tag_name'][f"{language}"]
                )

            return JsonResponse({'CREATE COMPANY NAME' : result,}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY ERROR'}, status = 400)
        
        except ValueError:
            return JsonResponse({'MESSAGE' : 'VALUE ERROR'}, status = 400)






        

