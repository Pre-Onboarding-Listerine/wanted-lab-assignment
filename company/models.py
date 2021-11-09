from django.db import models

class Company(models.Model):
    tags = models.ManyToManyField('Tag', through='CompanyTag', blank=True)

    class Meta:
        db_table = 'companies'

class CompanyTag(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tag     = models.ForeignKey('Tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companytags'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tags'

class CompanyName(models.Model):
    name    = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    lang    = models.CharField(max_length=100)

    class Meta:
        db_table = 'company_names'
