

from django.core.mail import EmailMessage
email = EmailMessage('Subject', 'Body', to=['mocomauricio@gmail.com'])
email.send()
