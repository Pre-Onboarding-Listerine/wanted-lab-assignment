import json

from django.views import View
from django.http import JsonResponse

from company.models import Company, CompanyName, Tag, CompanyTag


class CompanyView(View):
    def post(self, request):
        user_lang = request.headers.get('x-wanted-language', 'ko')
        data = json.loads(request.body)

        company_names = data.get('company_name')
        tags = data.get('tags')

        company = Company.objects.create()

        for co_lang, co_name in company_names.items():
            CompanyName.objects.create(name=co_name, lang=co_lang, company=company)

        for tag in tags:
            for tag_lang, tag_name in tag['tag_name'].items():
                new_tag = Tag.objects.create(lang=tag_lang, name=tag_name)
                CompanyTag.objects.create(company_id=company.id, tag_id=new_tag.id)

        ret_data = {
            'company_name': company_names[user_lang],
            'tags': [tag['tag_name'][user_lang] for tag in tags]
        }

        return JsonResponse(data=ret_data, status=201)

    def get(self, request):
        user_lang = request.headers.get('x-wanted-language', 'ko')
        keyword = request.GET.get('query', '')

        company_names = CompanyName.objects.filter(name__icontains=keyword)

        results = [
            {'company_name': company_name.name}
            for company_name in company_names
            if company_name.lang == user_lang
        ]
        return JsonResponse(data={'data': results}, status=200)


class SearchCompanyView(View):
    def get(self, request, keyword):
        user_lang = request.headers.get('x-wanted-language', 'ko')

        try:
            company_name = CompanyName.objects.get(name=keyword)
        except CompanyName.DoesNotExist:
            return JsonResponse({'message': 'company not found'}, status=404)
        else:
            user_company_name = CompanyName.objects.get(company_id=company_name.company.id, lang=user_lang)
            company_info = {
                'company_name': user_company_name.name,
                'tags': [tag.name for tag in user_company_name.company.tags.all() if tag.lang == user_lang]
            }
            return JsonResponse(data=company_info, status=200)
