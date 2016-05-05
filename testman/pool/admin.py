from django.contrib import admin
from .models import Domain

# add custom action to export CSV file
import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)
	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# writer a first row with header informaiton
	writer.writerow([field.verbose_name for field in fields])
	# Write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_description = 'Export to CSV'


class DomainAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'created', 'updated')
	list_filter = ('id', 'name')
	search_fields = ['id', 'name']
	actions = [export_to_csv]

admin.site.register(Domain, DomainAdmin)

from .models import Feature, Requirement, TestCase

class RequirementInline(admin.TabularInline):
	model = Requirement

class FeatureAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'function', 'description', 'created', 'updated')
	inlines = [RequirementInline,]

admin.site.register(Feature, FeatureAdmin)

from .models import Function, System
admin.site.register(Function)
admin.site.register(System)

from .models import TestStep, Composition
admin.site.register(TestStep)
admin.site.register(Composition)
admin.site.register(TestCase)