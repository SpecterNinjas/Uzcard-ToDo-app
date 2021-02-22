# Uzcard-ToDo-app
<strong>Description:</strong></br>
Simple ToDo app with an integrated set of Django applications addressing authentication, registration, account management as well as 3rd part social account authentication.

<strong>Requrement list:</strong></br>
1.pip install django (For Django installation) </br>
2.pip install django-crispy-forms (Handling Django Crispy Forms) </br>
3.pip install django-allauth (3rd party authentication - Google,Facebook,VK, etc)</br>


<strong>Main Components:</strong></br>
-TODO app that implements all CRUD (Create, Read, Update, Delete) functions</br>
-Registration(email, username, password)</br>
-Login (username, password, remember_me (for session))</br>
-Change/Reset Email/Password forms are avilable. (Email is to be sent for password reset/change. By clicking token-based url, user can change profile.)</br>


<strong>Email Configuration:</strong></br>
-Email is sent to user's for changing/resetting password.</br>
-Email verification is switched off, to turn in on goto uzcard_todo/settings.py and change the following: ACCOUNT_EMAIL_VERIFICATION = "mandatory".</br>
-Email includes token-based url for security purposes which is sent during profile change and email verification.</br>
---Email confirmation expires in 1 day (by default). To alter it goto uzcard_todo/settings.py and change the following: ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = ANY_INTEGER_NUMBER.</br>

*Email is sent by developer's gmail account, during deployment it's advised to integrate with Twilio Send Grid (https://sendgrid.com/docs/for-developers/sending-email/django/). </br>


<strong>Admin Page:</strong></br>
Goto: http://127.0.0.1:8000/admin/login/?next=/admin/</br>

Username: azam </br>
Password: Shilpildoq99#
