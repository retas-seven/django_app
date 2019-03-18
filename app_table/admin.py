from django.contrib import admin
from .models import Shohin
from .models import Company
from .models import Nohin
from .models import NohinDetail

# Register your models here.
admin.site.register(Shohin)
admin.site.register(Company)

class NohinDetailInline(admin.StackedInline):
    model = NohinDetail
    extra = 3

class NohinAdmin(admin.ModelAdmin):
    inlines = [NohinDetailInline]

admin.site.register(Nohin, NohinAdmin)
admin.site.register(NohinDetail)