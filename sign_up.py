# https://bingotingo.com/best-social-media-platforms/
# ---------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import PhotoImage
import smtplib
from random import randint
import re
import mysql.connector
from validate_email import validate_email
import string
import time
import bcrypt
# ---------------------------------------------------------------------------------------------------------
database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="20092009",
  database="app"
)
cursor = database.cursor()
# ---------------------------------------------------------------------------------------------------------
app = Tk()
app.geometry('1120x700+250+10')
app.title("sign up")
app.config(background='#F7F5FA')
app.iconbitmap(R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\sign_up_icon.ico')
# ---------------------------------------------------------------------------------------------------------
VerificationCode = randint(111111, 999999)
# ---------------------------------------------------------------------------------------------------------
# Button_Format
Button_Format_One = {
        'bg' : '#6946DD',
        'fg' : '#6946DD',
        'width' : 340,
        'font' : ("Gotham", 16,),
        'bd' : 0,
        'activebackground': '#6946DD',
        'activeforeground': '#6946DD',
        'anchor' : 'center',
        'repeatdelay':50,
        'compound' : 'center'
    }
Button_Format_Two = {
        'bg' : '#F7F5FA',
        'fg' : '#F7F5FA',
        'width' : 540,
        'font' : ("Gotham", 16),
        'bd' : 0,
        'activebackground': '#F7F5FA',
        'activeforeground': '#F7F5FA',
        'anchor' : 'center',
        'repeatdelay':50,
        'compound' : 'center'
    }
# Title_Format
Title_Login_Format = {
    'anchor' : 'w',
    'fg' : '#F7F5FA',
    'bg' : '#6946DD',
    'font' : ("Gotham", 35,'bold'),
    'width' : 12,
    'height' : 1,
    'bd' : 0,
}

Title_Sign_Up_Format = {
    'anchor' : 'w',
    'fg' : '#6946DD',
    'bg' : '#F7F5FA',
    'font' : ("Gotham", 35,'bold'),
    'width' : 12,
    'height' : 1,
    'bd' : 0,
}
# Back_Button_Format
Image_Back_Button = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Back_Button.png')
Back_Button_Format = {
    'activebackground' : '#F6F6F6',
    'relief' : 'flat',
    'bg' : '#F6F6F6',
    'repeatdelay' : 1,
    'image' : Image_Back_Button,
}
# Label_Format
Label_Format_One = {
   'fg' : '#F7F5FA',
   'bg' : '#6946DD',
   'font': ('Gotham',18)
}

Label_Format_Two = {
   'fg' : '#6946DD',
   'bg' : '#F7F5FA',
   'font': ('Gotham',18) 
}
# Error_Format
Error_Format = {
    'fg' : '#e60000',
    'bg' : '#F7F5FA', 
    'font' : ("Gotham", 12)
}
# Entry_Format
Entry_Format_One = {
    'fg' : 'black',
    'bg' : '#6946DD',
    'width' : 17,
    'bd' : 0,
    'font' : ("Gotham", 18),
    'justify' : 'center',
    'exportselection' : False,
    'insertbackground' : 'black',
    'insertwidth' : 1,
    'insertofftime' : 500,
    'insertontime' : 500,
    'relief' : 'flat',
    'selectbackground' : '#8887f5',
    'selectforeground' : 'red',
    # 'show' : '*',
    # 'validate' : None,
    # 'validatecommand' : None,
}

Entry_Format_Two = {
    'fg' : 'black',
    'bg' : '#F7F5FA',
    'width' : 10,
    'bd' : 0,
    'font' : ("Gotham", 18),
    'justify' : 'center',
    'exportselection' : True,
    'insertbackground' : 'black',
    'insertwidth' : 1,
    'insertofftime' : 500,
    'insertontime' : 500,
    'relief' : 'flat',
    'selectbackground' : '#8887f5',
    'selectforeground' : 'red',
    # 'show' : '*',
    # 'validate' : None,
    # 'validatecommand' : None,
}
# ---------------------------------------------------------------------------------------------------------
def Command_Button_sign_up ():
    global get_Entry_Last_Name
    global get_Entry_Password
    global get_Entry_Email
    global get_Entry_Password
    get_Entry_Last_Name = str(Entry_Last_Name.get()).strip()
    get_Entry_Password = str(Entry_Password.get()).strip()
    get_Entry_Confirm_Password = str(Entry_Confirm_Password.get()).strip()
    get_Entry_First_Name = str(Entry_First_Name.get()).strip()
    get_Entry_Email = str(Entry_Email.get()).strip()
    
    Validity = True
    
    Email_Validity = (validate_email(get_Entry_Email))
# ---------------------------------------------------------------------------------------------------------
    # Email
    if len(get_Entry_Email) == 0: #1
        Validity = False
        Error_Email_Two.place_forget()
        Error_Email_One.place(x=515,y=371)
    else:
        Error_Email_One.place_forget()
        if Email_Validity != True :
            Validity = False
            Error_Email_One.place_forget()
            Error_Email_Two.place(x=515,y=371)
        else:
            Error_Email_Two.place_forget()
    # First_Name
    if len(get_Entry_First_Name) == 0: #1
        Validity = False
        Error_First_Name_Two.place_forget()
        Error_First_Name_One.place(x=515,y=262)
    else:
        Error_First_Name_One.place_forget()
        
        for char in get_Entry_First_Name: #2
            if char in string.punctuation or char in string.digits:
                Validity = False
                Error_First_Name_One.place_forget()
                Error_First_Name_Two.place(x=515,y=262)
                break
            else :
                Error_First_Name_Two.place_forget()

    # Last_Name
    if len(get_Entry_Last_Name) == 0: #1
        Validity = False
        Error_Last_Name_Two.place_forget()
        Error_Last_Name_One.place(x=775,y=262)
    else :
        Error_Last_Name_One.place_forget()
        for char in get_Entry_Last_Name :#2
            if char in string.punctuation or char in string.digits:
                Validity = False
                Error_Last_Name_One.place_forget()
                Error_Last_Name_Two.place(x=775,y=262)
                break
            else :
                Error_Last_Name_Two.place_forget()
    # Password
    if len(get_Entry_Password) == 0 :
        Validity = False
        Error_password_Two.place_forget()
        Error_Confirm_Password_One.place_forget()
        Error_Confirm_Password_Two.place_forget()
        Error_password_One.place(x=515,y=480)
    else:
        Error_password_One.place_forget()
        if len(get_Entry_Password) < 8 \
        or set(get_Entry_Password).intersection(string.ascii_uppercase) == set()\
        or set(get_Entry_Password).intersection(string.ascii_lowercase) == set() \
        or set(get_Entry_Password).intersection(string.digits) == set()\
        or set(get_Entry_Password).intersection(string.punctuation) == set():
            Validity = False
            Error_password_One.place_forget()
            Error_Confirm_Password_One.place_forget()
            Error_Confirm_Password_Two.place_forget()
            Error_password_Two.place(x=515,y=480)
        else :
            Error_password_Two.place_forget()
            if len(get_Entry_Confirm_Password) == 0 :
                Validity = False
                Error_password_One.place_forget()
                Error_password_Two.place_forget()
                Error_Confirm_Password_Two.place_forget()
                Error_Confirm_Password_One.place(x=775,y=480)
            else :
                Error_Confirm_Password_One.place_forget()
                if get_Entry_Password != get_Entry_Confirm_Password :
                    Validity = False
                    Error_password_One.place_forget()
                    Error_password_Two.place_forget()
                    Error_Confirm_Password_One.place_forget()
                    Error_Confirm_Password_Two.place(x=775,y=480)
                else :
                    Error_Confirm_Password_Two.place_forget()
        
    if Validity :
        def verification ():
            From_Email = 'abdrbbeh@gmail.com'
            To_Email = get_Entry_Email
            Password ='gnizfzddloegooni'
            Subject = f"Your verification code : {VerificationCode}"
            Text = f"""Hello ,{get_Entry_First_Name}.\n
        Your verification code : {VerificationCode}"""
            Massage = f"Subject: {Subject}\n\n{Text}"
            server = smtplib.SMTP ('smtp.gmail.com', 587)
            server.starttls ()
            server.login(From_Email,Password)
            try:
                server.sendmail(From_Email,To_Email,Massage)
            except:
                Email_Validity = False
            finally:
                server.quit()
            for widget in app.place_slaves():
                widget.place_forget()
            app.title("verification")
            global Image_Verification
            global Image_Button_Verification
            Image_Verification = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Verification.png')
            Image_Verification_Lable = Label(app,bg='#6946DD',image=Image_Verification)
            Image_Verification_Lable.place(x=-2,y=-2)
        
            Image_Button = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Button_Sign_Up.png')
                
            Title_sign_up_Two = Label(app,cnf=Title_Sign_Up_Format,text="Verification")
            Title_sign_up_Two.place(x=625,y=175)

            Label_Verification = Label(app,text="Enter the verification code sent \nto your email ",cnf=Label_Format_Two,justify=LEFT)
            Label_Verification.place(x=625,y=250)

            Entry_Verification = Entry(app,cnf=Entry_Format_Two,width=18)
            Entry_Verification.place(x=667,y=313)
            
            Button_arrow_Three = Button(app,cnf=Back_Button_Format,command=sign_up)
            Button_arrow_Three.place(x=1040,y=0)

            def Command_Button_Verification():
                if str(Entry_Verification.get()) == str(VerificationCode) :
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(get_Entry_Password.encode("utf-8"), salt)
                    
                    sql = "INSERT INTO `Users` (`Email`, `First_Name`, `Last_Name`, `Password`) VALUES (%s, %s, %s, %s)"
                    values = (get_Entry_Email, get_Entry_First_Name, get_Entry_Last_Name, hashed_password)

                    cursor.execute(sql, values)
                    database.commit()
                    database.close()
                else:
                    Error_Verification = Label(app,text="The code you entered is incorrect.",cnf=Error_Format)
                    Error_Verification.place(x=630,y=350)
                    
            
            Image_Button_Verification = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Button_Verification.png')
            Button_Verification = Button(app,cnf=Button_Format_Two,text='verification',width=350,image=Image_Button_Verification,command=Command_Button_Verification)
            Button_Verification.place(x=630,y=385)
        verification()
# ---------------------------------------------------------------------------------------------------------
def Command_Button_Login ():
    pass
# ---------------------------------------------------------------------------------------------------------
def Command_Forgot_Password ():
    pass
# ---------------------------------------------------------------------------------------------------------
def sign_up ():
    for widget in app.place_slaves():
        widget.place_forget()
        
    global Entry_Email
    global Entry_Confirm_Password
    global Entry_First_Name
    global Entry_Last_Name
    global Entry_Password
    
    global Image_Sign_Up
    global Image_Button
    
    global Error_Email_One
    global Error_Email_Two
    global Error_First_Name_One
    global Error_First_Name_Two
    global Error_Last_Name_One
    global Error_Last_Name_Two
    global Error_password_One
    global Error_password_Two
    global Error_Confirm_Password_One
    global Error_Confirm_Password_Two 
    
    app.title("sign up")

    Image_Sign_Up = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Sign_Up.png')
    Image_Sign_Up_Lable = Label(app,bg='#6946DD',image=Image_Sign_Up)
    Image_Sign_Up_Lable.place(x=-2,y=-2)
    
    Image_Button = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Button_Sign_Up.png')
    
    Title_sign_up_One = Label(app,cnf=Title_Sign_Up_Format,text="Create Account")
    Title_sign_up_One.place(x=515,y=100)
    # First_Name
    Label_First_Name = Label(app,text="First name",cnf=Label_Format_Two)
    Label_First_Name.place(x=515,y=185)
    Entry_First_Name = Entry(app,cnf=Entry_Format_Two)
    Entry_First_Name.place(x=550,y=223)
    Error_First_Name_One = Label(app,text="Please enter your first name.",cnf=Error_Format)
    Error_First_Name_Two = Label(app,text="Please enter a valid name.",cnf=Error_Format)


    # Last_Name
    Lable_Last_Name = Label(app,text="Last name",cnf=Label_Format_Two)
    Lable_Last_Name.place(x=775,y=185)

    Entry_Last_Name = Entry(app,cnf=Entry_Format_Two)
    Entry_Last_Name.place(x=810,y=223)
    Error_Last_Name_One = Label(app,text="Please enter your last name.",cnf=Error_Format)
    Error_Last_Name_Two = Label(app,text="Please enter a valid name.",cnf=Error_Format)
    
    # Email
    Lable_Email = Label(app,text="Enter your email",cnf=Label_Format_Two)
    Lable_Email.place(x=515,y=295)
    
    Entry_Email = Entry(app,cnf=Entry_Format_Two,width=25)
    Entry_Email.place(x=556,y=331)
    Error_Email_One = Label(app,text="Please enter your email.",cnf=Error_Format)
    Error_Email_Two = Label(app,text="Please enter a valid email.",cnf=Error_Format)

    # Password
    Label_Password = Label(app,text="Password",cnf=Label_Format_Two)
    Label_Password.place(x=515,y=405)

    Entry_Password = Entry(app,cnf=Entry_Format_Two,show='*')
    Entry_Password.place(x=553,y=441)
    Error_password_One = Label(app,text="Please enter password.",cnf=Error_Format)
    Error_password_Two = Label(app,text="Password must be eight characters including one uppercase, one special character and alphanumeric characters.",cnf=Error_Format,wraplength=500,justify='left')
    # Confirm_Password
    Error_Confirm_Password_One = Label(app,text="Please enter your password confirmation.",cnf=Error_Format,wraplength=250,justify='left')
    Error_Confirm_Password_Two = Label(app,text="password does not match.",cnf=Error_Format)
    Label_Confirm_Password = Label(app,text="Confirm password",cnf=Label_Format_Two)
    Label_Confirm_Password.place(x=775,y=405)

    Entry_Confirm_Password = Entry(app,cnf=Entry_Format_Two,show='*')
    Entry_Confirm_Password.place(x=813,y=441)
    # Button
    Button_sign_up_Two = Button(app,cnf=Button_Format_Two,text='Create Account',image=Image_Button,command=Command_Button_sign_up)
    Button_sign_up_Two.place(x=480,y=525)

    Button_arrow_One = Button(app,cnf=Back_Button_Format,command=home)
    Button_arrow_One.place(x=1040,y=0)
    
    
# ---------------------------------------------------------------------------------------------------------
def Login ():
    for widget in app.place_slaves():
        widget.place_forget()
    global Image_Login
    global Image_Button
    app.title("Login")
    for widget in app.place_slaves():
        widget.place_forget()
        
    Image_Login = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Login.png')
    Image_Login_Lable = Label(app,bg='#6946DD',image=Image_Login)
    Image_Login_Lable.place(x=-2,y=-2)
    
    Image_Button = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Button.png')

    Title_Login_One = Label(app,cnf=Title_Login_Format,text="Welcome Back")
    Title_Login_One.place(x=100,y=150)

    Lable_Email_Login = Label(app,text="E-mail",cnf=Label_Format_One)
    Lable_Email_Login.place(x=115,y=225)
    
    Entry_Email_Login = Entry(app,cnf=Entry_Format_One)
    Entry_Email_Login.place(x=152,y=268)

    Label_Password_Login = Label(app,text="Password",cnf=Label_Format_One)
    Label_Password_Login.place(x=115,y=313)
    
    Entry_Password_Login = Entry(app,cnf=Entry_Format_One,show='*')
    Entry_Password_Login.place(x=152,y=356)
    
    Button_Login_Two = Button(app,cnf=Button_Format_One,text='Login',image=Image_Button,compound=CENTER,command=Login)
    Button_Login_Two.place(x=112,y=420)

    Button_arrow_Two = Button(app,cnf=Back_Button_Format,command=home)
    Button_arrow_Two.place(x=1040,y=0)
    
    Button_Forgot_Password = Button(app,text='Forgot your password?',cnf=Button_Format_One,fg='#F7F5FA',width=20,command=Command_Forgot_Password)
    Button_Forgot_Password.place(x=105,y=475)

# ---------------------------------------------------------------------------------------------------------
def home ():
    global Image_Home
    global Image_Button
    
    app.title("sign up")
    
    Image_Home = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Home.png')
    Image_Home_Lable = Label(app,bg='#6946DD',image=Image_Home)
    Image_Home_Lable.place(x=-2,y=-2)
 
    Image_Button = PhotoImage(file=R'C:\Users\USER\Downloads\Compressed\Odin3_v3.14.4\new\Python_Folder\sign_up\Image_Button.png')
    
    Button_sign_up_One = Button(app,cnf=Button_Format_One,image=Image_Button,text='Sign up',compound=CENTER,command=sign_up)
    Button_sign_up_One.place(x=75,y=275)
    
    Button_Login_One = Button(app,cnf=Button_Format_One,text='Login',image=Image_Button,compound=CENTER,command=Login)
    Button_Login_One.place(x=75,y=335)

home()
# ---------------------------------------------------------------------------------------------------------
app.mainloop()
