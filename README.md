# project_web_flask

## TN Store
Member: 

TRẦN ĐỨC TOÀN (Leader)

LÊ THỊ THANH NGÂN

🔑 Prerequisites
All the dependencies and required libraries are included in the file requirements.txt
🚀  Installation
1. Clone the repo
```
$ git clone https://github.com/To1nTr3n/project_web_flask.git
```
2. Change your directory to the cloned repo
```
$ cd project_web_flask\web\myenv\bin
```
3. Access a Python virtual environment named 'myenv' and activate it
```
$ activate
```
4. Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
$ cd ../../
```
```
$ pip install -r requirements.txt
```
💡 Working
1. You access config.py and edit
```
ADMINS = ['your-email@gmail.com'] #your-email
```
2. Open terminal/cmd. Go into the cloned project directory and type the following command:
```
$ set MAIL_SERVER=smtp.googlemail.com
$ set MAIL_PORT=587
$ set MAIL_USE_TLS=1
$ set MAIL_USERNAME= <your_email@gmail.com>
$ set MAIL_PASSWORD= <your_password>
```

```
$ flask run
```

# Note: google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to this link while you're logged in to your google account, and allow the access:
- https://www.google.com/settings/security/lesssecureapps
![image](https://user-images.githubusercontent.com/65596323/143179043-015ec854-ab31-46d2-b5e1-f39046f41888.png)

- https://accounts.google.com/DisplayUnlockCaptcha
![image](https://user-images.githubusercontent.com/65596323/143179076-40f9cebf-e4b5-431d-bbf3-13eeedaf9487.png)


