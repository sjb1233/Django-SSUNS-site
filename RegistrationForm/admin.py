from django.contrib import admin
from import_export import resources
# Register your models here
#from core.models import RegistrationForm
from .forms import RegForm
from .models import RegistrationForm
from import_export.admin import ImportExportActionModelAdmin

from .forms import InputForm
from .models import DelegateInput

from .forms import PositionPaperForm
from .models import PositionPaper

from .forms import CountryAssignmentForm
from .models import CountryAssignment


class RegistrationResource(resources.ModelResource):
	list_display = ["__unicode__", "date","Faculty_Advisor_Name", "Name_of_School"]
	class Meta:
		model = RegistrationForm

class RegistrationFormAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "date","Faculty_Advisor_Name", "Name_of_School"]
	# form = RegForm
	class Meta:
		model = RegistrationForm
class RegistrationFormAdmin(ImportExportActionModelAdmin):
	# exclude = ('Will_this_be_your_first_time_attending_SSUNS','Faculty_Advisor_Alternate_Email', 'Cell_Phone', 'Head_Delegate_Name','Cell_Phone_of_Head_Delegate', 'Head_Delegate_Email', 'Address_Line_1', 'Address_Line_2', 'City', 'Province_or_State_or_Region','Country','Phone','Fax','Are_there_any_allergies_or_concerns_that_we_should_know_about', 'Please_Specify', 'Media_Consent',)
	list_display = ["__unicode__", "date","Faculty_Advisor_Name", "Name_of_School"]
	# form = RegForm
	class Meta:
		model = RegistrationForm
	pass
class InputFormAdmin(ImportExportActionModelAdmin):
	list_display = ["Name_of_School"]
	class Meta:
		model = DelegateInput

class PositionPaperAdmin(ImportExportActionModelAdmin):
	list_display = ["Name_of_School", "Your_Country", "Your_Committee"]

class CountryAssignmentAdmin(ImportExportActionModelAdmin):
	list_display = ["Faculty_Advisor_Email"]

admin.site.register(RegistrationForm, RegistrationFormAdmin)
admin.site.register(DelegateInput, InputFormAdmin)
admin.site.register(PositionPaper, PositionPaperAdmin)
admin.site.register(CountryAssignment, CountryAssignmentAdmin)
