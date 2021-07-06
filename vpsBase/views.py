from django.shortcuts import render
from .forms import Contact_form
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def home(request):
    return render(request, 'vpsBase/index.html')

def contact(request): 
    if request.method == "POST":
        cf = Contact_form(request.POST)
        sg = sendgrid.SendGridAPIClient(api_key="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")
        from_email = Email("harshverma9102@gmail.com")  # Change to your verified sender
        to_email = To("vpsparsarmabihar@gmail.com")  # Change to your recipient
        subject = "Sending with SendGrid is Fun"
        content = Content("text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, to_email, subject, content)

        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        return render(request, 'vpsBase/contact.html', { 'success_msg': "Thank you for contacting us. We will get back to you soon.", 'form': cf })
        print(response.status_code)
        print(response.headers)
    cf = Contact_form()
    return render(request, 'vpsBase/contact.html', {'form': cf})
