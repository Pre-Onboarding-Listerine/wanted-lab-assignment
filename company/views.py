import json

from django.views import View
from django.http import JsonResponse

from company.models import Company, CompanyName, Tag, CompanyTag


class CreateCompanyView(View):
    def post(self, request):
        user_lang = request.headers.get('x-wanted-language', 'ko')
        data = json.loads(request.body)

        company_names = data.get('company_name')
        tags = data.get('tags')

        company = Company.objects.create()

        for co_lang, co_name in company_names.items():
            CompanyName.objects.create(name=co_name, lang=co_lang, company=company)

        for tag in tags:
            for tag_lang, tag_name in tag.items():
                new_tag = Tag.objects.create(lang=tag_lang, name=tag_name)
                CompanyTag.objects.create(company_id=company.id, tag_id=new_tag.id)

        ret_data = {
            'company_name': company_names[user_lang],
            'tags': [tag['tag_name'][user_lang] for tag in tags]
        }

        return JsonResponse(data=ret_data, status=201)
