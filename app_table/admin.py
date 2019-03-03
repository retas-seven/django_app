from django.contrib import admin
from .models import Shohin
from .models import Company
from .models import Nohin
from .models import NohinDetail

# Register your models here.
admin.site.register(Shohin)
admin.site.register(Company)
admin.site.register(Nohin)
admin.site.register(NohinDetail)
