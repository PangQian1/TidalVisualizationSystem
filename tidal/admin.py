from django.contrib import admin

# Register your models here.
from tidal import models

admin.site.register(models.GridAttr)
admin.site.register(models.DateGrid)