

from django.core.mail import EmailMessage
email = EmailMessage('Subject', 'Body', to=['sigestrec@gmail.com'])
email.send()

