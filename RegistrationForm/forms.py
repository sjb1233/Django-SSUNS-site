from django import forms

from .models import RegistrationForm
from .models import DelegateInput
from .models import PositionPaper
from .models import CountryAssignment
class RegForm(forms.ModelForm):
	class Meta:
		model = RegistrationForm
		fields = ['Name_of_School', 'Will_this_be_your_first_time_attending_SSUNS', 'Faculty_Advisor_Name', 'Faculty_Advisor_Email', 'Faculty_Advisor_Alternate_Email', 'Cell_Phone', 'Head_Delegate_Name','Cell_Phone_of_Head_Delegate', 'Head_Delegate_Email', 'Address_Line_1', 'Address_Line_2', 'City', 'Province_or_State_or_Region','Country','Phone','Fax', 'General_Assemblies_and_ECOSOC', 'Specialized_Agencies', 'Crises' , 'Previous_Model_UN_Experience', 'Number_of_Delegates', 'Payment_Method', 'Are_there_any_allergies_or_concerns_that_we_should_know_about', 'Please_Specify', 'Media_Consent'  ]

		widgets = {
		# 'Number_of_Delegates': forms.Select(attrs={'onchange': 'this.form.submit()'})
            # 'Will_this_be_your_first_time_attending_SSUNS': forms.RadioSelect
        }

	def clean_Faculty_Advisor_Email(self):
		email = self.cleaned_data.get('Faculty_Advisor_Email')
		# Use below if you want to run further tests on 'email'
		# if not "text" in email:
			# raise forms.ValidationError("Error_message")
		return email

	def clean_Faculty_Advisor_Name(self):
		Faculty_Advisor_Name = self.cleaned_data.get('Faculty_Advisor_Name')
		if not " " in Faculty_Advisor_Name:
			raise forms.ValidationError("Please enter: first name and last name")
		#first_name, last_name = full_name.split(" ")
		return Faculty_Advisor_Name

	def clean_Head_Delegate_Name(self):
		name = self.cleaned_data.get('Head_Delegate_Name')
		if not " " in name:
			raise forms.ValidationError("Please enter: first name and last name")
		return name

	def clean_Number_of_Delegates(self):
		numDels = self.cleaned_data.get('Number_of_Delegates')
		return numDels

	def clean_Payment_Method(self):
		payment = self.cleaned_data.get('Payment_Method')
		return payment	
	def clean_Name_of_School(self):
		school = self.cleaned_data.get('Name_of_School')
		return school

class InputForm(forms.ModelForm):
	class Meta:
		model = DelegateInput
		fields = ['Name_of_School', 
		'Delegate_1', 
		'Delegate_1_Country',
		'Delegate_1_Committee',
		'Delegate_2', 
		'Delegate_2_Country',
		'Delegate_2_Committee',
		'Delegate_3', 
		'Delegate_3_Country',
		'Delegate_3_Committee',
		'Delegate_4', 
		'Delegate_4_Country',
		'Delegate_4_Committee',
		'Delegate_5', 
		'Delegate_5_Country',
		'Delegate_5_Committee',
		'Delegate_6', 
		'Delegate_6_Country',
		'Delegate_6_Committee',
		'Delegate_7', 
		'Delegate_7_Country',
		'Delegate_7_Committee',
		'Delegate_8', 
		'Delegate_8_Country',
		'Delegate_8_Committee',
		'Delegate_9', 
		'Delegate_9_Country',
		'Delegate_9_Committee',
		'Delegate_10', 
		'Delegate_10_Country',
		'Delegate_10_Committee',
		'Faculty_Advisor_1_Name',
		'Faculty_Advisor_2_Name',
		'Faculty_Advisor_3_Name',
		'Faculty_Advisor_4_Name',
		'Faculty_Advisor_5_Name']
	def clean_Name_of_School(self):
		school = self.cleaned_data.get('Name_of_School')
		inBackend = False
		for item in RegistrationForm.objects.all():
			if school == item.Name_of_School:
				inBackend = True
				break
		if inBackend == False:
			raise forms.ValidationError("School name not recognized. Please ensure the name is spelt correctly (including capitals and spacing)")
		return school

class PositionPaperForm(forms.ModelForm):
	class Meta:
		model = PositionPaper
		fields = ['Name_of_School', 'Your_Name', 'Your_Committee', 'Your_Country', 'file']
	def clean_Name_of_School(self):
		school = self.cleaned_data.get('Name_of_School')
		inBackend = False
		for item in RegistrationForm.objects.all():
			if school.strip() == item.Name_of_School.strip():
				inBackend = True
				break
		if inBackend == False:
			raise forms.ValidationError("School name not recognized. Please ensure the name is spelt correctly (including capitals and spacing)")
		return school

class CountryAssignmentForm(forms.ModelForm):
	class Meta:
		model = CountryAssignment
		fields = ['Faculty_Advisor_Email', 
		'Country_1', 'Country_1_Committee_1','Country_1_Committee_2','Country_1_Committee_3','Country_1_Committee_4','Country_1_Committee_5','Country_1_Committee_6','Country_1_Committee_7','Country_1_Committee_8','Country_1_Committee_9',
		'Country_2', 'Country_2_Committee_1','Country_2_Committee_2','Country_2_Committee_3','Country_2_Committee_4','Country_2_Committee_5','Country_2_Committee_6','Country_2_Committee_7','Country_2_Committee_8','Country_2_Committee_9',
		'Country_3', 'Country_3_Committee_1','Country_3_Committee_2','Country_3_Committee_3','Country_3_Committee_4','Country_3_Committee_5','Country_3_Committee_6','Country_3_Committee_7','Country_3_Committee_8','Country_3_Committee_9',
		'Country_4', 'Country_4_Committee_1','Country_4_Committee_2','Country_4_Committee_3','Country_4_Committee_4','Country_4_Committee_5','Country_4_Committee_6','Country_4_Committee_7','Country_4_Committee_8','Country_4_Committee_9',
		'Country_5', 'Country_5_Committee_1','Country_5_Committee_2','Country_5_Committee_3','Country_5_Committee_4','Country_5_Committee_5','Country_5_Committee_6','Country_5_Committee_7','Country_5_Committee_8','Country_5_Committee_9',
		'Country_6', 'Country_6_Committee_1','Country_6_Committee_2','Country_6_Committee_3','Country_6_Committee_4','Country_6_Committee_5','Country_6_Committee_6','Country_6_Committee_7','Country_6_Committee_8','Country_6_Committee_9',
		'Country_7', 'Country_7_Committee_1','Country_7_Committee_2','Country_7_Committee_3','Country_7_Committee_4','Country_7_Committee_5','Country_7_Committee_6','Country_7_Committee_7','Country_7_Committee_8','Country_7_Committee_9',
		'Country_8', 'Country_8_Committee_1','Country_8_Committee_2','Country_8_Committee_3','Country_8_Committee_4','Country_8_Committee_5','Country_8_Committee_6','Country_8_Committee_7','Country_8_Committee_8','Country_8_Committee_9',
		'Country_9', 'Country_9_Committee_1','Country_9_Committee_2','Country_9_Committee_3','Country_9_Committee_4','Country_9_Committee_5','Country_9_Committee_6','Country_9_Committee_7','Country_9_Committee_8','Country_9_Committee_9',
		'Country_10', 'Country_10_Committee_1','Country_10_Committee_2','Country_10_Committee_3','Country_10_Committee_4','Country_10_Committee_5','Country_10_Committee_6','Country_10_Committee_7','Country_10_Committee_8','Country_10_Committee_9',
		'Country_11', 'Country_11_Committee_1','Country_11_Committee_2','Country_11_Committee_3','Country_11_Committee_4','Country_11_Committee_5','Country_11_Committee_6','Country_11_Committee_7','Country_11_Committee_8','Country_11_Committee_9',
		'Country_12', 'Country_12_Committee_1','Country_12_Committee_2','Country_12_Committee_3','Country_12_Committee_4','Country_12_Committee_5','Country_12_Committee_6','Country_12_Committee_7','Country_12_Committee_8','Country_12_Committee_9',
		'Country_13', 'Country_13_Committee_1','Country_13_Committee_2','Country_13_Committee_3','Country_13_Committee_4','Country_13_Committee_5','Country_13_Committee_6','Country_13_Committee_7','Country_13_Committee_8','Country_13_Committee_9',
		'Country_14', 'Country_14_Committee_1','Country_14_Committee_2','Country_14_Committee_3','Country_14_Committee_4','Country_14_Committee_5','Country_14_Committee_6','Country_14_Committee_7','Country_14_Committee_8','Country_14_Committee_9',
		'Country_15', 'Country_15_Committee_1','Country_15_Committee_2','Country_15_Committee_3','Country_15_Committee_4','Country_15_Committee_5','Country_15_Committee_6','Country_15_Committee_7','Country_15_Committee_8','Country_15_Committee_9']
	def clean_Faculty_Advisor_Email(self):
		email = self.cleaned_data.get('Faculty_Advisor_Email')
		inBackend = False
		for item in RegistrationForm.objects.all():
			if email.strip() == item.Faculty_Advisor_Email.strip():
				inBackend = True
				break
		if inBackend == False:
			raise forms.ValidationError("Email does not exist")
		return email
		
