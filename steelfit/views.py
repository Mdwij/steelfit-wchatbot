from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
def index(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def about(request):
    return render(request, "about.html")

def product(request):
    return render(request, "product.html")

def infrastructure(request):
    return render(request, "infrastructure.html")

def certificates(request):
    return render(request, "certificates.html")

def clients(request):
    return render(request, "clients.html")

def contact(request):
    return render(request, "contact.html")

def dishend(request):
    return render(request, "dishend.html")

def cones(request):
    return render(request, "cones.html")

def pipecap(request):
    return render(request, "pipecap.html")

def bending(request):
    return render(request, "bending.html")

def tori(request):
    return render(request, "cones.html")

def swage(request):
    return render(request, "swage connection.html")

def bellow(request):
    return render(request, "bellow.html")

@xframe_options_sameorigin
def chatbot(request):
    return render(request, "chatbot.html")




def pop(request):
    return render(request, "popup.html")
from django.http import JsonResponse

# Django view
from django.shortcuts import render

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient, sender_email, sender_password):
    # Create message object instance
    message = MIMEMultipart()

    # Set the message body
    message.attach(MIMEText(body, 'plain'))

    # Set the message subject
    message['Subject'] = subject

    # Set the message recipient
    message['To'] = recipient

    # Set the message sender
    message['From'] = sender_email

    # Connect to the SMTP server and send the message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()



def fnc_for_name(all_vars):
    all_vars["user_name"] = all_vars['user_input']
    all_vars["name_enterd"] = "true"
    all_vars["response"] = ["Name noted. Now enter your company name."]
    return all_vars

def fnc_for_company(all_vars):
    all_vars["company_enterd"] = "true"
    all_vars["user_company"] = all_vars['user_input']
    all_vars["response"] = ["Your Company name noted. Now please enter your phone number."]
        
    return all_vars

def fnc_for_phone(all_vars):
    all_vars["phone_enterd"] = "true"
    all_vars["user_phone"] = all_vars['user_input']
    all_vars["response"] = ["Your Phone Number noted",
                            "Now please choose the product type from below."]
        
    return all_vars

def reset_vars(all_vars):
    all_vars['response'] = ['Hello!', 'Please Enter your name.']
    all_vars['hi_done'] = "false"
    all_vars['specifications'] = "false"
    all_vars['name_enterd'] = "false"
    all_vars['user_name'] = ""
    all_vars['company_enterd'] = "false"
    all_vars['user_company'] = ""
    all_vars['phone_enterd'] = "false"
    all_vars['user_phone'] = ""
    all_vars['product_enterd'] = "false"
    all_vars['user_product'] = ""
    all_vars['specification_enterd'] = "false"
    all_vars['user_specification'] = ""
    all_vars['everything_enterd'] = "false"
    return all_vars

def note_info_and_send_mail(all_vars):
    all_vars["everything_enterd"] = "true"
    out = "\nName: " + all_vars["user_name"] + "\nCompany Name: " + all_vars["user_company"] + "\nPhone Number: " + all_vars["user_phone"] + "\nProduct Wanted: " + all_vars["user_product"] + "\nSpecifications of Product: " + all_vars["user_specification"]   
    if 'yes' in all_vars["user_input"]:
        all_vars = reset_vars(all_vars)
        send_email("New Enquiry", out, "steelfitengg@gmail.com", "steel.fit123@gmail.com", "bndknnudyeshzodt")
        all_vars['response'] = ["Everything Noted and email was sent to owner describing your requirements","Please Enter hi to restart the conversation"]
    elif 'no' in all_vars["user_input"]:
        all_vars = reset_vars(all_vars)
        all_vars['hi_done'] = "true"
    else:
        all_vars['response'] = ["Below is information stated by you",out,"Is information is completely correct?"]
    return all_vars

def chatbot_response(request):
    user_input = request.GET.get('user_input', '').lower()
    hi_done = request.GET.get('hi_done','')
    specifications = request.GET.get('specifications', '').lower()
    name_enterd = request.GET.get('name_enterd', '').lower()
    user_name = request.GET.get('user_name', '').lower()
    company_enterd = request.GET.get('company_enterd', '').lower()
    user_company = request.GET.get('user_company', '').lower()
    phone_enterd = request.GET.get('phone_enterd', '').lower()
    user_phone = request.GET.get('user_phone', '').lower()
    product_enterd = request.GET.get('product_enterd', '').lower()
    user_product = request.GET.get('user_product', '').lower()
    specification_enterd = request.GET.get('specification_enterd', '').lower()
    user_specification = request.GET.get('user_specification', '').lower()
    everything_enterd = request.GET.get('everything_enterd', '').lower()

    all_vars = {'response': [''],
                'user_input': user_input,
                'hi_done':hi_done,
                'specifications':specifications,
                "name_enterd":name_enterd,
                'user_name':user_name,
                "company_enterd":company_enterd,
                'user_company':user_company,
                "phone_enterd":phone_enterd,
                'user_phone':user_phone,
                "product_enterd":product_enterd,
                'user_product':user_product,
                "specification_enterd":specification_enterd,
                'user_specification':user_specification,
                'everything_enterd':everything_enterd}

    if all_vars["user_input"] == 'hi':
        all_vars = reset_vars(all_vars)
        all_vars['hi_done'] = "true"
        return JsonResponse(all_vars)
    
    if all_vars["hi_done"] == "true":

        if all_vars["name_enterd"] == "true":
            if all_vars["company_enterd"] == "true":

                if all_vars['phone_enterd'] == "true":

                    if all_vars['product_enterd'] == "true":

                        if specification_enterd == "true":
                            if everything_enterd == "false":
                                all_vars["user_specification"] = all_vars["user_input"]
                                all_vars["user_input"] = "kk"
                            all_vars = note_info_and_send_mail(all_vars)  
                        else:
                            all_vars["response"] = ["Please enter your specifications if any otherwise enter 'none'."]
                            all_vars["specification_enterd"] = "true"

                else:
                    all_vars=fnc_for_phone(all_vars)
            else:
                all_vars = fnc_for_company(all_vars)
            
        
        else:
            all_vars = fnc_for_name(all_vars)

    else:
        all_vars["response"] = ["please type hi to start the conversation"]

    return JsonResponse(all_vars)
