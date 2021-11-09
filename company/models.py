from django.db import models
from django.db.models.deletion import CASCADE

from core.models import TimeStampModel

class Company(TimeStampModel):
    company_name = models.JSONField(max_length=128, null=True)

    class Meta:
        db_table = 'companies'

class Tag(TimeStampModel):
    tag_name = models.JSONField(max_length=100, null=True)
    company  = models.ForeignKey('Company',on_delete=CASCADE)

    class Meta:
        db_table = 'tags'



# class CompanyName(TimeStampModel):
#     name     = models.CharField(max_length=128, null=True)
#     language = models.CharField(max_length=4, null=True)
#     company  = models.ForeignKey('Company', on_delete=CASCADE)

#     class Meta:
#         db_table = 'company_names'

# class Company(TimeStampModel):
#     tags = models.ManyToManyField('Tag', through='CompanyTag', null=True)

#     class Meta:
#         db_table = 'companies'

# class CompanyTag(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     tag     = models.ForeignKey('Tag', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'companytags'

# class Tag(TimeStampModel):
#     name     = models.CharField(max_length=100, null=True)
#     language = models.CharField(max_length=4, null=True)

#     class Meta:
#         db_table = 'tags'

