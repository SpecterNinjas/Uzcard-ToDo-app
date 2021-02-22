# Uzcard-ToDo-app
Simple ToDo app with an integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

<strong>Requrement list:</strong>
1.pip install django (For Django installation) 
2.pip install django-crispy-forms (Handling Django Crispy Forms) 
3.pip install django-allauth (3rd party authentication - Google,Facebook,VK, etc)


<strong>Main Components:</strong>
-TODO app that implements all CRUD (Create, Read, Update, Delete) functions
-Registration(email, username, password)
-Login (username, password, remember_me (for session))
-Change/Reset Email/Password forms are avilable. (Email is to be sent for password reset/change. By clicking token-based url, user can change profile.)


<strong>Email Configuration:</strong>
-Email is sent to user's for changing/resetting password.
-Email verification is switched off, to turn in on goto uzcard_todo/settings.py and change the following: ACCOUNT_EMAIL_VERIFICATION = "mandatory".
-Email includes token-based url for security purposes which is sent during profile change and email verification.
---Email confirmation expires in 1 day (by default). To alter it goto uzcard_todo/settings.py and change the following: ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = ANY_INTEGER_NUMBER.

*Email is sent by developer's gmail account, during deployment it's advised to integrate with Twilio Send Grid (https://sendgrid.com/docs/for-developers/sending-email/django/).


<strong>Admin Page:</strong>
Goto: http://127.0.0.1:8000/admin/login/?next=/admin/

Username:azam </br>
Password:Shilpildoq99#
