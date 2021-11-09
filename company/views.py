import json

from django.views import View
from django.http import JsonResponse
from company.models import Tag, Company

class CompanyCreateView(View):
    #새로운 회사 추가할 것

    #1 . date raw로 데이터 베이스에 저장하고 
    #2 . tw값만 return 해준다. 
    def post(self, request):
        try:
            language = request.headers.get("x-wanted-language", "ko")
            
            #1 . date raw로 데이터 베이스에 저장하고 
            data = json.loads(request.body)
            company_name = data["company_name"]
            tag_name = data["tags"]
            #중복된 값있으면 잡을 것===== 

            company =Company.objects.create(company_name = company_name)
            
            tag = Tag.objects.create(
                tag_name = tag_name,
                company_id = company.id
            )

    #2 . tw값만 return 해준다. 
            result = {
                "company_name" : company.company_name[f"{language}"],
                "tags" : []
            }
            tag_list = tag.tag_name
            for i in range(len(tag_list)):
                result["tags"].append(
                    tag_list[i]['tag_name'][f"{language}"]
                )

            return JsonResponse({'MESSAGE' : 'CREATE COMPANY NAME'},result, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY ERROR'}, status = 400)
        
        except ValueError:
            return JsonResponse({'MESSAGE' : 'VALUE ERROR'}, status = 400)






        

