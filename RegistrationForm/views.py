from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegForm
from django.conf import settings
from .models import RegistrationForm
from .forms import InputForm
from .models import PositionPaper
from .forms import PositionPaperForm
from .models import DelegateInput
from .forms import InputForm
from .models import CountryAssignment
from .forms import CountryAssignmentForm

# Create your views here.
def CountryAssignmentView(request):
  form = CountryAssignmentForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    email = form.cleaned_data.get("Faculty_Advisor_Email")
    instance.save()
    return HttpResponseRedirect('/countryassignment')
  context = {
    "form": form
  }
  return render(request, "assignmentForm.html", context)



def positionpaper(request):
  if not request.user.is_authenticated():
    return render(request, "index.html", {})
  form = PositionPaperForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    instance = form.save(commit=False)
    school = form.cleaned_data.get("Name_of_School")
    instance.save()
    return HttpResponseRedirect('/')

  context = {
    "form": form
  }
  return render(request, "positionpaper.html", context)

def DelegateInputView(request):
  if not request.user.is_authenticated():
    return render(request, "index.html", {})
  form = InputForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    school = form.cleaned_data.get("Name_of_School")
    instance.save()
    return HttpResponseRedirect('/DelegateInput/')
  context = {
    "form": form
  }
  return render(request, "DelegateInput.html", context)

def profile(request):
  if not request.user.is_authenticated():
    return render(request, "index.html", {})
  #Grab log-in user's info:
  NumDels = None 
  School = None
  FAName = None
  PaymentMethod = None
  PaidInvoice = None
  CountryAssignmentString = ""
  if request.user.is_authenticated():
    userEmail = request.user.email.strip()
    for item in RegistrationForm.objects.all():
      email = item.Faculty_Advisor_Email.strip()
      if email == userEmail:
        NumDels = str(item.Number_of_Delegates)
        School = item.Name_of_School
        FAName = item.Faculty_Advisor_Name
        if item.Payment_Method == False:
          PaymentMethod = "Cheque by Mail"
        else:
          PaymentMethod = "Paypal"
        if item.Paid == False:
          PaidInvoice = "We haven't received your payment yet"
        else:
          PaidInvoice = "Yes"
    for item in CountryAssignment.objects.all():
      email = item.Faculty_Advisor_Email.strip()
      if email == userEmail:
        for i in range(1,16):
          countryField = "Country_" + str(i)
          field = getattr(item, countryField)
          if field == None or field == "":
            continue
          CountryAssignmentString = CountryAssignmentString + "<b>" + str(field) + "</b>: "
          for j in range(1,10):
            committeeField = "Country_" + str(i) + "_Committee_" + str(j)
            nextCommitteeField = "Country_" + str(i) + "_Committee_" + str(j+1)
            val = getattr(item, committeeField)
            if val == None or val == "":
              continue
            if j == 9:
              CountryAssignmentString = CountryAssignmentString + str(val) + "<br/>"
              break
            nextVal = getattr(item, nextCommitteeField)
            if nextVal == None or nextVal == "":
              CountryAssignmentString = CountryAssignmentString + str(val) + "<br/>"
              break
            CountryAssignmentString = CountryAssignmentString + str(val) + ", "



  if NumDels == None:
    NumDels = ""
  
  if School == None:
    School = ""
  
  if FAName == None:
    FAName = ""
  
  if PaymentMethod == None:
    PaymentMethod = ""
  
  if PaidInvoice == None:
    PaidInvoice = ""

  error = None

  if NumDels == "" or School == "" or FAName == "" or PaymentMethod == "" or PaidInvoice == "":
    error = "There was an error in grabbing your information. Please try loggin on again. If the error persists, email the USG-IT at it@ssuns.org"
  else:
    error = ""

  positionPapers = []
  for item in PositionPaper.objects.all():
    if School.strip() == item.Name_of_School.strip():
      positionPapers.append(item.Your_Name)
  Inputs = []
  for item in DelegateInput.objects.all():
    if School.strip() == item.Name_of_School.strip():
      if item.Delegate_1 != None and item.Delegate_1 != "":
        Inputs.append(item.Delegate_1 + " - " + item.Delegate_1_Committee)
      if item.Delegate_2 != None and item.Delegate_2 != "":
        Inputs.append(item.Delegate_2 + " - " + item.Delegate_2_Committee)
      if item.Delegate_3 != None and item.Delegate_3 != "":
        Inputs.append(item.Delegate_3 + " - " + item.Delegate_3_Committee)
      if item.Delegate_4 != None and item.Delegate_4 != "":
        Inputs.append(item.Delegate_4 + " - " + item.Delegate_4_Committee)
      if item.Delegate_5 != None and item.Delegate_5 != "":
        Inputs.append(item.Delegate_5 + " - " + item.Delegate_5_Committee)
      if item.Delegate_6 != None and item.Delegate_6 != "":
        Inputs.append(item.Delegate_6 + " - " + item.Delegate_6_Committee)
      if item.Delegate_7 != None and item.Delegate_7 != "":
        Inputs.append(item.Delegate_7 + " - " + item.Delegate_7_Committee)
      if item.Delegate_8 != None and item.Delegate_8 != "":
        Inputs.append(item.Delegate_8 + " - " + item.Delegate_8_Committee)
      if item.Delegate_9 != None and item.Delegate_9 != "":
        Inputs.append(item.Delegate_9 + " - " + item.Delegate_9_Committee)
      if item.Delegate_10 != None and item.Delegate_10 != "":
        Inputs.append(item.Delegate_10 + " - " + item.Delegate_10_Committee)
      if item.Faculty_Advisor_1_Name != None and item.Faculty_Advisor_1_Name != "":
        Inputs.append(item.Faculty_Advisor_1_Name.upper())
      if item.Faculty_Advisor_2_Name != None and item.Faculty_Advisor_2_Name != "":
        Inputs.append(item.Faculty_Advisor_2_Name.upper())
      if item.Faculty_Advisor_3_Name != None and item.Faculty_Advisor_3_Name != "":
        Inputs.append(item.Faculty_Advisor_3_Name.upper())
      if item.Faculty_Advisor_4_Name != None and item.Faculty_Advisor_4_Name != "":
        Inputs.append(item.Faculty_Advisor_4_Name.upper())
      if item.Faculty_Advisor_5_Name != None and item.Faculty_Advisor_5_Name != "":
        Inputs.append(item.Faculty_Advisor_5_Name.upper())
  context = {
    "NumDels": NumDels,
    "School": School,
    "FAName": FAName,
    "PaymentMethod": PaymentMethod,
    "PaidInvoice": PaidInvoice,
    "PositionPapers": ", ".join(positionPapers),
    "Inputs": "<br/> ".join(Inputs),
    "error": error,
    "CountryAssignmentString": CountryAssignmentString
  }
  return render(request, "profile.html", context)


def registration(request):


	# if request.method == "POST":
	# 	print request.POST

  form = RegForm(request.POST or None)
  NumberDels = form['Number_of_Delegates'].value()
  if form.is_valid():
    instance = form.save(commit=False)
    identification = form.cleaned_data.get("Name_of_School")
    #NumDels = form.cleaned_data.get("Number_of_Delegates")
    #One can put validations here
    NumDels = int(form.cleaned_data.get("Number_of_Delegates"))
    FAemail = form.cleaned_data.get("Faculty_Advisor_Email")
    Faculty_Advisor_Name = form.cleaned_data.get("Faculty_Advisor_Name")
    paypalTF = form.cleaned_data.get("Payment_Method") #True if paypal, false if cheque
    subject = 'SSUNS 2017 Registration'
    from_email = settings.EMAIL_HOST_USER
    to_email = [FAemail, 'it@ssuns.org', 'schools@ssuns.org', 'finance@ssuns.org', 'sg@ssuns.org']
    totalCost = 85*NumDels + 85
    paypal = 1.03*(85*NumDels + 85)
    if not paypalTF:
      contact_message = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge" /><!--<![endif]-->
    <meta name="viewport" content="width=device-width" />
    <title> </title>
    <style type="text/css">
.btn a:hover,
.footer__links a:hover {
  opacity: 0.8;
}
.wrapper .footer__share-button:hover {
  color: #ffffff !important;
  opacity: 0.8;
}
a[x-apple-data-detectors] {
  color: inherit !important;
  text-decoration: none !important;
  font-size: inherit !important;
  font-family: inherit !important;
  font-weight: inherit !important;
  line-height: inherit !important;
}
.column {
  padding: 0;
  text-align: left;
  vertical-align: top;
}
.mso .font-avenir,
.mso .font-cabin,
.mso .font-open-sans,
.mso .font-ubuntu {
  font-family: sans-serif !important;
}
.mso .font-bitter,
.mso .font-merriweather,
.mso .font-pt-serif {
  font-family: Georgia, serif !important;
}
.mso .font-lato,
.mso .font-roboto {
  font-family: Tahoma, sans-serif !important;
}
.mso .font-pt-sans {
  font-family: "Trebuchet MS", sans-serif !important;
}
.mso .footer p {
  margin: 0;
}
@media only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min--moz-device-pixel-ratio: 2), only screen and (-o-min-device-pixel-ratio: 2/1), only screen and (min-device-pixel-ratio: 2), only screen and (min-resolution: 192dpi), only screen and (min-resolution: 2dppx) {
  .fblike {
    background-image: url(https://i7.createsend1.com/static/eb/customise/13-the-blueprint-3/images/fblike@2x.png) !important;
  }
  .tweet {
    background-image: url(https://i8.createsend1.com/static/eb/customise/13-the-blueprint-3/images/tweet@2x.png) !important;
  }
  .linkedinshare {
    background-image: url(https://i9.createsend1.com/static/eb/customise/13-the-blueprint-3/images/lishare@2x.png) !important;
  }
  .forwardtoafriend {
    background-image: url(https://i10.createsend1.com/static/eb/customise/13-the-blueprint-3/images/forward@2x.png) !important;
  }
}
@media only screen and (max-width: 620px) {
  .wrapper .size-18,
  .wrapper .size-20 {
    font-size: 17px !important;
    line-height: 26px !important;
  }
  .wrapper .size-22 {
    font-size: 18px !important;
    line-height: 26px !important;
  }
  .wrapper .size-24 {
    font-size: 20px !important;
    line-height: 28px !important;
  }
  .wrapper .size-26 {
    font-size: 22px !important;
    line-height: 31px !important;
  }
  .wrapper .size-28 {
    font-size: 24px !important;
    line-height: 32px !important;
  }
  .wrapper .size-30 {
    font-size: 26px !important;
    line-height: 34px !important;
  }
  .wrapper .size-32 {
    font-size: 28px !important;
    line-height: 36px !important;
  }
  .wrapper .size-34,
  .wrapper .size-36 {
    font-size: 30px !important;
    line-height: 38px !important;
  }
  .wrapper .size-40 {
    font-size: 32px !important;
    line-height: 40px !important;
  }
  .wrapper .size-44 {
    font-size: 34px !important;
    line-height: 43px !important;
  }
  .wrapper .size-48 {
    font-size: 36px !important;
    line-height: 43px !important;
  }
  .wrapper .size-56 {
    font-size: 40px !important;
    line-height: 47px !important;
  }
  .wrapper .size-64 {
    font-size: 44px !important;
    line-height: 50px !important;
  }
  .divider {
    Margin-left: auto !important;
    Margin-right: auto !important;
  }
  .btn a {
    display: block !important;
    font-size: 14px !important;
    line-height: 24px !important;
    padding: 12px 10px !important;
    width: auto !important;
  }
  .btn--shadow a {
    padding: 12px 10px 13px 10px !important;
  }
  .image img {
    height: auto;
    width: 100%%;
  }
  .layout,
  .column,
  .preheader__webversion,
  .header td,
  .footer,
  .footer__left,
  .footer__right,
  .footer__inner {
    width: 320px !important;
  }
  .preheader__snippet,
  .layout__edges {
    display: none !important;
  }
  .preheader__webversion {
    text-align: center !important;
  }
  .layout--full-width {
    width: 100%% !important;
  }
  .layout--full-width tbody,
  .layout--full-width tr {
    display: table;
    Margin-left: auto;
    Margin-right: auto;
    width: 320px;
  }
  .column,
  .layout__gutter,
  .footer__left,
  .footer__right {
    display: block;
    Float: left;
  }
  .footer__inner {
    text-align: center;
  }
  .footer__links {
    Float: none;
    Margin-left: auto;
    Margin-right: auto;
  }
  .footer__right p,
  .footer__share-button {
    display: inline-block;
  }
  .layout__gutter {
    font-size: 20px;
    line-height: 20px;
  }
  .layout--no-gutter.layout--has-border:not(.layout--full-width),
  .layout--has-gutter.layout--has-border .column__background {
    width: 322px !important;
  }
  .layout--has-gutter.layout--has-border {
    left: -1px;
    position: relative;
  }
}
@media only screen and (max-width: 320px) {
  .border {
    display: none;
  }
  .layout--no-gutter.layout--has-border:not(.layout--full-width),
  .layout--has-gutter.layout--has-border .column__background {
    width: 320px !important;
  }
  .layout--has-gutter.layout--has-border {
    left: 0 !important;
  }
}
</style>
    
  <!--[if !mso]><!--><style type="text/css">
@import url(https://fonts.googleapis.com/css?family=Cabin:400,700,400italic,700italic|Open+Sans:400italic,700italic,700,400);
</style><link href="https://fonts.googleapis.com/css?family=Cabin:400,700,400italic,700italic|Open+Sans:400italic,700italic,700,400" rel="stylesheet" type="text/css" /><!--<![endif]--><style type="text/css">
body,.wrapper{background-color:#f5f7fa}.wrapper h1{color:#44a8c7;font-size:26px;line-height:34px}.wrapper h1{}.wrapper h1{font-family:Cabin,Avenir,sans-serif}.mso .wrapper h1{font-family:sans-serif !important}.wrapper h2{color:#44a8c7;font-size:20px;line-height:28px}.wrapper h3{color:#434547;font-size:16px;line-height:24px}.wrapper a{color:#5c91ad}.wrapper a:hover{color:#375a6c !important}@media only screen and (max-width: 620px){.wrapper h1{}.wrapper h1{font-size:22px;line-height:31px}.wrapper h2{}.wrapper h2{font-size:17px;line-height:26px}.wrapper h3{}.wrapper p{}}.column,.column__background td{color:#60666d;font-size:14px;line-height:21px}.column,.column__background td{font-family:"Open Sans",sans-serif}.mso .column,.mso .column__background td{font-family:sans-serif 
!important}.border{background-color:#b1c1d8}.layout--no-gutter.layout--has-border:not(.layout--full-width),.layout--has-gutter.layout--has-border .column__background,.layout--full-width.layout--has-border{border-top:1px solid #b1c1d8;border-bottom:1px solid #b1c1d8}.wrapper blockquote{border-left:4px solid #b1c1d8}.divider{background-color:#b1c1d8}.wrapper .btn a{color:#fff}.wrapper .btn a{font-family:"Open Sans",sans-serif}.mso .wrapper .btn a{font-family:sans-serif !important}.wrapper .btn a:hover{color:#fff !important}.btn--flat a,.btn--shadow a,.btn--depth a{background-color:#5c91ad}.btn--ghost a{border:1px solid #5c91ad}.preheader--inline,.footer__left{color:#b9b9b9}.preheader--inline,.footer__left{font-family:"Open Sans",sans-serif}.mso .preheader--inline,.mso .footer__left{font-family:sans-serif !important}.wrapper .preheader--inline a,.wrapper .footer__left 
a{color:#b9b9b9}.wrapper .preheader--inline a:hover,.wrapper .footer__left a:hover{color:#b9b9b9 !important}.header__logo{color:#c3ced9}.header__logo{font-family:Roboto,Tahoma,sans-serif}.mso .header__logo{font-family:Tahoma,sans-serif !important}.wrapper .header__logo a{color:#c3ced9}.wrapper .header__logo a:hover{color:#859bb1 !important}.footer__share-button{background-color:#7b7c7d}.footer__share-button{font-family:"Open Sans",sans-serif}.mso .footer__share-button{font-family:sans-serif !important}.layout__separator--inline{font-size:20px;line-height:20px;mso-line-height-rule:exactly}
</style><meta name="robots" content="noindex,nofollow" />
<meta property="og:title" content="My First Campaign" />
</head>
<!--[if mso]>
  <body class="mso">
<![endif]-->
<!--[if !mso]><!-->
  <body class="full-padding" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%%;background-color: #f5f7fa;">
<!--<![endif]-->
    <div class="wrapper" style="background-color: #f5f7fa;">
      <table style='border-collapse: collapse;table-layout: fixed;color: #b9b9b9;font-family: "Open Sans",sans-serif;' align="center">
        <tbody><tr>
          <td class="preheader__snippet" style="padding: 10px 0 5px 0;vertical-align: top;width: 280px;">
            <p style="Margin-top: 0;Margin-bottom: 0;font-size: 12px;line-height: 19px;">SSUNS 2017 Registration</p>
          </td>
          <td class="preheader__webversion" style="text-align: right;padding: 10px 0 5px 0;vertical-align: top;width: 280px;">
            
          </td>
        </tr>
      </tbody></table>
      <table class="header" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;" align="center" id="emb-email-header-container">
        <tbody><tr>
          <td style="padding: 0;width: 600px;">
            <div class="header__logo emb-logo-margin-box" style="font-size: 26px;line-height: 32px;Margin-top: 0px;Margin-bottom: 20px;color: #c3ced9;font-family: Roboto,Tahoma,sans-serif;Margin-left: 20px;Margin-right: 20px;">
              <div class="logo-center" style="font-size:0px !important;line-height:0 !important;" align="center" id="emb-email-header"><img style="height: auto;width: 100%%;border: 0;max-width: 200px;" src="http://www.dragonacademy.org/wp-content/uploads/2015/11/logo-SSUNS.png" alt="" width="200" height="190" /></div>
            </div>
          </td>
        </tr>
      </tbody></table>
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #307fb0;background-position: 0px 0px;background-image: url(https://i1.createsend1.com/ei/d/3C/814/26C/020854/csfinal/montrealdusk.jpg);background-repeat: repeat;" align="center">
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 600px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <div style="line-height:55px;font-size:1px">&nbsp;</div>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;">
      <h1 class="size-40" style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 40px;line-height: 47px;font-family: Cabin,Avenir,sans-serif;text-align: center;"><span style="color:#f5f7fa"><strong>SSUNS Priority Registration</strong></span></h1><p class="size-20" style="Margin-top: 20px;Margin-bottom: 20px;font-size: 20px;line-height: 28px;text-align: center;"><span style="color:#f5f7fa"><font color="#ffffff">Thank you for registering for SSUNS 2017</font></span></p>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <div style="line-height:40px;font-size:1px">&nbsp;</div>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 600px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <div style="line-height:10px;font-size:1px">&nbsp;</div>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <h2 class="size-24" style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 24px;line-height: 32px;text-align: center;"><strong> SSUNS Invoice: %s </strong> <br/><br/> <strong>Payment Method: Mail</strong></h2>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;">Hey %s: we look forward to having you and your delegation join us in November for another great year of Model United Nations. &nbsp;&nbsp;</p>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;"><b>Payment Breakdown:</b><br/> <br/> <b>Cost Per Delegate</b> (Regular): $85 ........ $%s.00 / %s delegates</p>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;"><b>Delegation Fee:</b> (Regular): $85 ........ $85.00 per delegation</p>


    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;Margin-bottom: 24px;">
        <div class="image" style="font-size: 12px;font-style: normal;font-weight: 400;" align="center">
          <img style="display: block;border: 0;max-width: 480px;" src="http://storage.torontosun.com/v1/dynamic_resize/sws_path/suns-prod-images/1297784799942_ORIGINAL.jpg?quality=80&size=420x" alt="" width="260" height="173" />
        </div>
      </div>
    
          </td>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;Margin-bottom: 24px;">
      <h2 style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 20px;line-height: 28px;"><strong>Payment by Mail</strong></h2><p style="Margin-top: 16px;Margin-bottom: 0;"><strong>Total: %d.00</strong></p><p style="Margin-top: 20px;Margin-bottom: 0;">Please make&nbsp;the cheque&nbsp;out to IRSAM (International Relations Students' Association of McGill) at the address:</p><p style="Margin-top: 20px;Margin-bottom: 0;">IRSAM Inc.; 3480 Rue McTavish, Suite 410; Montreal, QC, Canada H3A 1X9</p>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
        <div class="image" style="font-size: 12px;font-style: normal;font-weight: 400;Margin-bottom: 20px;" align="center">
          <img style="display: block;border: 0;max-width: 480px;" src="http://bestdelegate.com/wp-content/uploads/2014/11/Screen-Shot-2014-12-01-at-10.18.21-PM.png" alt="" width="260" height="195" />
        </div>
      </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <p style="Margin-top: 0;Margin-bottom: 0;">
    </p></div>
    
          </td>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <h2 style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 20px;line-height: 28px;"><strong>Delegate Change or Info</strong></h2><p style="Margin-top: 16px;Margin-bottom: 20px;">If you need to change the number of delegates coming with your delegation, or you have a question, please use the button below to send an email to the relevant secretariat members.</p>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <div class="btn btn--flat" style="text-align:left;">
        <![if !mso]><a style="border-radius: 4px;display: inline-block;font-weight: bold;text-align: center;text-decoration: none !important;transition: opacity 0.1s ease-in;color: #fff;background-color: #5c91ad;font-family: 'Open Sans', sans-serif;font-size: 12px;line-height: 22px;padding: 10px 28px;" href="mailto:it@ssuns.org,schools@ssuns.org,finance@ssuns.org,sg@ssuns.org" data-width="192">Delegate Change or Information</a><![endif]>
      <!--[if mso]><p style="line-height:0;margin:0;">&nbsp;</p><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="mailto:it@ssuns.org,schools@ssuns.org,finance@ssuns.org,sg@ssuns.org" style="width:248px" arcsize="10%%" fillcolor="#5C91AD" stroke="f"><v:textbox style="mso-fit-shape-to-text:t" inset="0px,9px,0px,9px"><center style="font-size:12px;line-height:22px;color:#FFFFFF;font-family:sans-serif;font-weight:bold;mso-line-height-rule:exactly;mso-text-raise:4px">Delegate Change or Information</center></v:textbox></v:roundrect><![endif]--></div>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="footer" style="border-collapse: collapse;table-layout: fixed;Margin-right: auto;Margin-left: auto;border-spacing: 0;width: 560px;" align="center">
        <tbody><tr>
          <td style="padding: 0 0 40px 0;">
            <table class="footer__right" style="border-collapse: collapse;table-layout: auto;border-spacing: 0;" align="right">
              <tbody><tr>
                <td class="footer__inner" style="padding: 0;">
                  
                  
                  
                  
                </td>
              </tr>
            </tbody></table>
            <table class="footer__left" style='border-collapse: collapse;table-layout: fixed;border-spacing: 0;color: #b9b9b9;font-family: "Open Sans",sans-serif;width: 380px;'>
              <tbody><tr>
                <td class="footer__inner" style="padding: 0;font-size: 12px;line-height: 19px;">
                  
                  <div>
                    <div>Secondary School Model United Nations Symposium 2017</div>
                  </div>
                  <div class="footer__permission" style="Margin-top: 18px;">
                    
                  </div>
                  <div>
                  </div>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
      </tbody></table>
      
    </div>
  
</body></html>"""%(str(identification),Faculty_Advisor_Name, str(NumDels*85), str(NumDels),totalCost)
    else:
      contact_message = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge" /><!--<![endif]-->
    <meta name="viewport" content="width=device-width" />
    <title> </title>
    <style type="text/css">
.btn a:hover,
.footer__links a:hover {
  opacity: 0.8;
}
.wrapper .footer__share-button:hover {
  color: #ffffff !important;
  opacity: 0.8;
}
a[x-apple-data-detectors] {
  color: inherit !important;
  text-decoration: none !important;
  font-size: inherit !important;
  font-family: inherit !important;
  font-weight: inherit !important;
  line-height: inherit !important;
}
.column {
  padding: 0;
  text-align: left;
  vertical-align: top;
}
.mso .font-avenir,
.mso .font-cabin,
.mso .font-open-sans,
.mso .font-ubuntu {
  font-family: sans-serif !important;
}
.mso .font-bitter,
.mso .font-merriweather,
.mso .font-pt-serif {
  font-family: Georgia, serif !important;
}
.mso .font-lato,
.mso .font-roboto {
  font-family: Tahoma, sans-serif !important;
}
.mso .font-pt-sans {
  font-family: "Trebuchet MS", sans-serif !important;
}
.mso .footer p {
  margin: 0;
}
@media only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min--moz-device-pixel-ratio: 2), only screen and (-o-min-device-pixel-ratio: 2/1), only screen and (min-device-pixel-ratio: 2), only screen and (min-resolution: 192dpi), only screen and (min-resolution: 2dppx) {
  .fblike {
    background-image: url(https://i7.createsend1.com/static/eb/customise/13-the-blueprint-3/images/fblike@2x.png) !important;
  }
  .tweet {
    background-image: url(https://i8.createsend1.com/static/eb/customise/13-the-blueprint-3/images/tweet@2x.png) !important;
  }
  .linkedinshare {
    background-image: url(https://i9.createsend1.com/static/eb/customise/13-the-blueprint-3/images/lishare@2x.png) !important;
  }
  .forwardtoafriend {
    background-image: url(https://i10.createsend1.com/static/eb/customise/13-the-blueprint-3/images/forward@2x.png) !important;
  }
}
@media only screen and (max-width: 620px) {
  .wrapper .size-18,
  .wrapper .size-20 {
    font-size: 17px !important;
    line-height: 26px !important;
  }
  .wrapper .size-22 {
    font-size: 18px !important;
    line-height: 26px !important;
  }
  .wrapper .size-24 {
    font-size: 20px !important;
    line-height: 28px !important;
  }
  .wrapper .size-26 {
    font-size: 22px !important;
    line-height: 31px !important;
  }
  .wrapper .size-28 {
    font-size: 24px !important;
    line-height: 32px !important;
  }
  .wrapper .size-30 {
    font-size: 26px !important;
    line-height: 34px !important;
  }
  .wrapper .size-32 {
    font-size: 28px !important;
    line-height: 36px !important;
  }
  .wrapper .size-34,
  .wrapper .size-36 {
    font-size: 30px !important;
    line-height: 38px !important;
  }
  .wrapper .size-40 {
    font-size: 32px !important;
    line-height: 40px !important;
  }
  .wrapper .size-44 {
    font-size: 34px !important;
    line-height: 43px !important;
  }
  .wrapper .size-48 {
    font-size: 36px !important;
    line-height: 43px !important;
  }
  .wrapper .size-56 {
    font-size: 40px !important;
    line-height: 47px !important;
  }
  .wrapper .size-64 {
    font-size: 44px !important;
    line-height: 50px !important;
  }
  .divider {
    Margin-left: auto !important;
    Margin-right: auto !important;
  }
  .btn a {
    display: block !important;
    font-size: 14px !important;
    line-height: 24px !important;
    padding: 12px 10px !important;
    width: auto !important;
  }
  .btn--shadow a {
    padding: 12px 10px 13px 10px !important;
  }
  .image img {
    height: auto;
    width: 100%%;
  }
  .layout,
  .column,
  .preheader__webversion,
  .header td,
  .footer,
  .footer__left,
  .footer__right,
  .footer__inner {
    width: 320px !important;
  }
  .preheader__snippet,
  .layout__edges {
    display: none !important;
  }
  .preheader__webversion {
    text-align: center !important;
  }
  .layout--full-width {
    width: 100%% !important;
  }
  .layout--full-width tbody,
  .layout--full-width tr {
    display: table;
    Margin-left: auto;
    Margin-right: auto;
    width: 320px;
  }
  .column,
  .layout__gutter,
  .footer__left,
  .footer__right {
    display: block;
    Float: left;
  }
  .footer__inner {
    text-align: center;
  }
  .footer__links {
    Float: none;
    Margin-left: auto;
    Margin-right: auto;
  }
  .footer__right p,
  .footer__share-button {
    display: inline-block;
  }
  .layout__gutter {
    font-size: 20px;
    line-height: 20px;
  }
  .layout--no-gutter.layout--has-border:not(.layout--full-width),
  .layout--has-gutter.layout--has-border .column__background {
    width: 322px !important;
  }
  .layout--has-gutter.layout--has-border {
    left: -1px;
    position: relative;
  }
}
@media only screen and (max-width: 320px) {
  .border {
    display: none;
  }
  .layout--no-gutter.layout--has-border:not(.layout--full-width),
  .layout--has-gutter.layout--has-border .column__background {
    width: 320px !important;
  }
  .layout--has-gutter.layout--has-border {
    left: 0 !important;
  }
}
</style>
    
  <!--[if !mso]><!--><style type="text/css">
@import url(https://fonts.googleapis.com/css?family=Cabin:400,700,400italic,700italic|Open+Sans:400italic,700italic,700,400);
</style><link href="https://fonts.googleapis.com/css?family=Cabin:400,700,400italic,700italic|Open+Sans:400italic,700italic,700,400" rel="stylesheet" type="text/css" /><!--<![endif]--><style type="text/css">
body,.wrapper{background-color:#f5f7fa}.wrapper h1{color:#44a8c7;font-size:26px;line-height:34px}.wrapper h1{}.wrapper h1{font-family:Cabin,Avenir,sans-serif}.mso .wrapper h1{font-family:sans-serif !important}.wrapper h2{color:#44a8c7;font-size:20px;line-height:28px}.wrapper h3{color:#434547;font-size:16px;line-height:24px}.wrapper a{color:#5c91ad}.wrapper a:hover{color:#375a6c !important}@media only screen and (max-width: 620px){.wrapper h1{}.wrapper h1{font-size:22px;line-height:31px}.wrapper h2{}.wrapper h2{font-size:17px;line-height:26px}.wrapper h3{}.wrapper p{}}.column,.column__background td{color:#60666d;font-size:14px;line-height:21px}.column,.column__background td{font-family:"Open Sans",sans-serif}.mso .column,.mso .column__background td{font-family:sans-serif 
!important}.border{background-color:#b1c1d8}.layout--no-gutter.layout--has-border:not(.layout--full-width),.layout--has-gutter.layout--has-border .column__background,.layout--full-width.layout--has-border{border-top:1px solid #b1c1d8;border-bottom:1px solid #b1c1d8}.wrapper blockquote{border-left:4px solid #b1c1d8}.divider{background-color:#b1c1d8}.wrapper .btn a{color:#fff}.wrapper .btn a{font-family:"Open Sans",sans-serif}.mso .wrapper .btn a{font-family:sans-serif !important}.wrapper .btn a:hover{color:#fff !important}.btn--flat a,.btn--shadow a,.btn--depth a{background-color:#5c91ad}.btn--ghost a{border:1px solid #5c91ad}.preheader--inline,.footer__left{color:#b9b9b9}.preheader--inline,.footer__left{font-family:"Open Sans",sans-serif}.mso .preheader--inline,.mso .footer__left{font-family:sans-serif !important}.wrapper .preheader--inline a,.wrapper .footer__left 
a{color:#b9b9b9}.wrapper .preheader--inline a:hover,.wrapper .footer__left a:hover{color:#b9b9b9 !important}.header__logo{color:#c3ced9}.header__logo{font-family:Roboto,Tahoma,sans-serif}.mso .header__logo{font-family:Tahoma,sans-serif !important}.wrapper .header__logo a{color:#c3ced9}.wrapper .header__logo a:hover{color:#859bb1 !important}.footer__share-button{background-color:#7b7c7d}.footer__share-button{font-family:"Open Sans",sans-serif}.mso .footer__share-button{font-family:sans-serif !important}.layout__separator--inline{font-size:20px;line-height:20px;mso-line-height-rule:exactly}
</style><meta name="robots" content="noindex,nofollow" />
<meta property="og:title" content="My First Campaign" />
</head>
<!--[if mso]>
  <body class="mso">
<![endif]-->
<!--[if !mso]><!-->
  <body class="full-padding" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%%;background-color: #f5f7fa;">
<!--<![endif]-->
    <div class="wrapper" style="background-color: #f5f7fa;">
      <table style='border-collapse: collapse;table-layout: fixed;color: #b9b9b9;font-family: "Open Sans",sans-serif;' align="center">
        <tbody><tr>
          <td class="preheader__snippet" style="padding: 10px 0 5px 0;vertical-align: top;width: 280px;">
            <p style="Margin-top: 0;Margin-bottom: 0;font-size: 12px;line-height: 19px;">SSUNS 2017 Registration</p>
          </td>
          <td class="preheader__webversion" style="text-align: right;padding: 10px 0 5px 0;vertical-align: top;width: 280px;">
            
          </td>
        </tr>
      </tbody></table>
      <table class="header" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;" align="center" id="emb-email-header-container">
        <tbody><tr>
          <td style="padding: 0;width: 600px;">
            <div class="header__logo emb-logo-margin-box" style="font-size: 26px;line-height: 32px;Margin-top: 0px;Margin-bottom: 20px;color: #c3ced9;font-family: Roboto,Tahoma,sans-serif;Margin-left: 20px;Margin-right: 20px;">
              <div class="logo-center" style="font-size:0px !important;line-height:0 !important;" align="center" id="emb-email-header"><img style="height: auto;width: 100%%;border: 0;max-width: 200px;" src="http://www.dragonacademy.org/wp-content/uploads/2015/11/logo-SSUNS.png" alt="" width="200" height="190" /></div>
            </div>
          </td>
        </tr>
      </tbody></table>
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #307fb0;background-position: 0px 0px;background-image: url(https://i1.createsend1.com/ei/d/3C/814/26C/020854/csfinal/montrealdusk.jpg);background-repeat: repeat;" align="center">
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 600px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <div style="line-height:55px;font-size:1px">&nbsp;</div>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;">
      <h1 class="size-40" style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 40px;line-height: 47px;font-family: Cabin,Avenir,sans-serif;text-align: center;"><span style="color:#f5f7fa"><strong>SSUNS Priority Registration</strong></span></h1><p class="size-20" style="Margin-top: 20px;Margin-bottom: 20px;font-size: 20px;line-height: 28px;text-align: center;"><span style="color:#f5f7fa"><font color="#ffffff">Thank you for registering for SSUNS 2017</font></span></p>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <div style="line-height:40px;font-size:1px">&nbsp;</div>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 600px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <div style="line-height:10px;font-size:1px">&nbsp;</div>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <h2 class="size-24" style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 24px;line-height: 32px;text-align: center;"> <strong> SSUNS Invoice: %s </strong><br/><br/><strong>Payment Method: Paypal</strong></h2>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;">Hey %s: we look forward to having you and your delegation join us in November for another great year of Model United Nations. &nbsp;&nbsp;</p>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;"><b>Payment Breakdown:</b><br/> <br/> <b>Cost Per Delegate</b> (Regular): $85 ........ $%s.00 / %s delegates</p>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;"><b>Delegation Fee:</b> (Regular): $85 ........ $85.00 per delegation</p>
      <p class="size-16" style="Margin-top: 16px;Margin-bottom: 0;font-size: 16px;line-height: 24px;text-align: center;"><b>Paypal Fee:</b> 3.00%% ........ 3.00%% for online transactions</p>
      </div>


      </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;Margin-bottom: 24px;">
        <div class="image" style="font-size: 12px;font-style: normal;font-weight: 400;" align="center">
          <img style="display: block;border: 0;max-width: 480px;" src="http://storage.torontosun.com/v1/dynamic_resize/sws_path/suns-prod-images/1297784799942_ORIGINAL.jpg?quality=80&size=420x" alt="" width="260" height="173" />
        </div>
      </div>
    
          </td>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;Margin-bottom: 24px;">
      <h2 style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 20px;line-height: 28px;"><strong>Payment by Paypal</strong></h2><p style="Margin-top: 16px;Margin-bottom: 0;"><strong>Total: %.2f</strong></p><p style="Margin-top: 20px;Margin-bottom: 0;"> The Under-Secretary-General of Finance will send you a paypal invoice shortly. The invoice will be sent to the Faculty Advisor email that you specified in the registration form.</p><p style="Margin-top: 20px;Margin-bottom: 0;"></p>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="layout layout--no-gutter" style="border-collapse: collapse;table-layout: fixed;Margin-left: auto;Margin-right: auto;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;" align="center" emb-background-style>
        <tbody><tr>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
        <div class="image" style="font-size: 12px;font-style: normal;font-weight: 400;Margin-bottom: 20px;" align="center">
          <img style="display: block;border: 0;max-width: 480px;" src="http://bestdelegate.com/wp-content/uploads/2014/11/Screen-Shot-2014-12-01-at-10.18.21-PM.png" alt="" width="260" height="195" />
        </div>
      </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <p style="Margin-top: 0;Margin-bottom: 0;">
    </p></div>
    
          </td>
          <td class="column" style='padding: 0;text-align: left;vertical-align: top;color: #60666d;font-size: 14px;line-height: 21px;font-family: "Open Sans",sans-serif;width: 300px;'>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-top: 24px;">
      <h2 style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #44a8c7;font-size: 20px;line-height: 28px;"><strong>Delegate Change or Info</strong></h2><p style="Margin-top: 16px;Margin-bottom: 20px;">If you need to change the number of delegates coming with your delegation, or you have a question, please use the button below to send an email to the relevant secretariat members.</p>
    </div>
    
            <div style="Margin-left: 20px;Margin-right: 20px;Margin-bottom: 24px;">
      <div class="btn btn--flat" style="text-align:left;">
        <![if !mso]><a style="border-radius: 4px;display: inline-block;font-weight: bold;text-align: center;text-decoration: none !important;transition: opacity 0.1s ease-in;color: #fff;background-color: #5c91ad;font-family: 'Open Sans', sans-serif;font-size: 12px;line-height: 22px;padding: 10px 28px;" href="mailto:it@ssuns.org,schools@ssuns.org,finance@ssuns.org,sg@ssuns.org" data-width="192">Delegate Change or Information</a><![endif]>
      <!--[if mso]><p style="line-height:0;margin:0;">&nbsp;</p><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="mailto:it@ssuns.org,schools@ssuns.org,finance@ssuns.org,sg@ssuns.org" style="width:248px" arcsize="10%%" fillcolor="#5C91AD" stroke="f"><v:textbox style="mso-fit-shape-to-text:t" inset="0px,9px,0px,9px"><center style="font-size:12px;line-height:22px;color:#FFFFFF;font-family:sans-serif;font-weight:bold;mso-line-height-rule:exactly;mso-text-raise:4px">Delegate Change or Information</center></v:textbox></v:roundrect><![endif]--></div>
    </div>
    
          </td>
        </tr>
      </tbody></table>
  
      <table class="footer" style="border-collapse: collapse;table-layout: fixed;Margin-right: auto;Margin-left: auto;border-spacing: 0;width: 560px;" align="center">
        <tbody><tr>
          <td style="padding: 0 0 40px 0;">
            <table class="footer__right" style="border-collapse: collapse;table-layout: auto;border-spacing: 0;" align="right">
              <tbody><tr>
                <td class="footer__inner" style="padding: 0;">
                  
                  
                  
                  
                </td>
              </tr>
            </tbody></table>
            <table class="footer__left" style='border-collapse: collapse;table-layout: fixed;border-spacing: 0;color: #b9b9b9;font-family: "Open Sans",sans-serif;width: 380px;'>
              <tbody><tr>
                <td class="footer__inner" style="padding: 0;font-size: 12px;line-height: 19px;">
                  
                  <div>
                    <div>Secondary School Model United Nations Symposium 2017</div>
                  </div>
                  <div class="footer__permission" style="Margin-top: 18px;">
                    
                  </div>
                  <div>
                  </div>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
      </tbody></table>
      
    </div>
  
</body></html>"""%(str(identification), Faculty_Advisor_Name, str(NumDels*85), str(NumDels), float(totalCost*1.03))

    message = """
  	%s: Thank you for registering for SSUNS 2017 via your email %s
  	Your total is going to come to $%d.00 
    """%(Faculty_Advisor_Name, FAemail, totalCost)


    send_mail(
      subject, #Subject
      message,
      from_email, #From
      to_email, #To [list]
      fail_silently=False,
      html_message=contact_message 
      )



    instance.save()
    return HttpResponseRedirect('/')



  context = {
    "form": form,
    "NumberDels": NumberDels,
  }
  return render(request, "form.html", context)


