from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class TemplateEmail:
    def __init__(self,subject, to, template_name, context=None):
        self.subject = subject
        self.to = to
        self.template_name = template_name
        self.context = context or {}

    def send(self):
        message = render_to_string(self.template_name,self.context)
        email = EmailMessage(
            self.subject,
            message,
            to=[self.to]
        )

        email.content_subtype = "html"
        email.send()