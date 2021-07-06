from django.shortcuts import render
from .forms import Contact_form
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def home(request):
    return render(request, 'vpsBase/index.html')

def contact(request): 
    if request.method == "POST":
        cf = Contact_form(request.POST)
        if cf.is_valid():
            full_name = cf.cleaned_data['first_name'] + " " + cf.cleaned_data['last_name']
            email = cf.cleaned_data['email']
            contact = cf.cleaned_data['contact']
            msg = cf.cleaned_data['message']
            sg = sendgrid.SendGridAPIClient(api_key="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")
            from_email = Email("harshverma9102@gmail.com")  # Change to your verified sender
            to_email = To("vpsparsarmabihar@gmail.com")  # Change to your recipient
            subject = "New Contact"
            content = Content("text/html", f"Name: <strong>{full_name}</strong><br/> Email: <strong>{email}</strong><br/> Contact: <strong>{contact}</strong><br/> Message: <strong>{msg}</strong>")
            mail = Mail(from_email, to_email, subject, content)

            mail_json = mail.get()
            response = sg.client.mail.send.post(request_body=mail_json)
            return render(request, 'vpsBase/contact.html', { 'success_msg': "Thank you for contacting us. We will get back to you soon.", 'form': cf })
            print(response.status_code)
            print(response.headers)
    cf = Contact_form()
    return render(request, 'vpsBase/contact.html', {'form': cf})
