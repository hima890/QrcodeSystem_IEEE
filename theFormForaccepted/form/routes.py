# the import part 
from flask import Blueprint, redirect, render_template, url_for, request, flash # import the flask main function
from theFormForaccepted import db # import the database
from models import theAccepted # import the database classs
from theFormForaccepted.form.utilty import newLinkGanaretor, FULL_PATH # import function from the utilty
from theFormForaccepted import mail, Message # impotr the mail function(send)
import os # import python os functions


home_page = Blueprint('home', __name__, static_folder='static', template_folder='templates') # blueprint name

@home_page.route("/", methods=["POST", "GET"]) # the main route accept get and post methods
@home_page.route("/home", methods=["POST", "GET"]) # the main route accept get and post methods
def index(): # function call when the route call
    if request.method == "POST": # when the mothod is post the fallown code well ex.
        full_name = request.form.get("full_name") # get the name value from the forme
        email = request.form.get("email") # get the email value from the forme

        query_check = theAccepted.query.filter_by(email=email).first() # check if the email address in the database
        if query_check: # if its in the database the system well relode the page with a flash message that show the erroe
            flash("The E-mail that you enter is alrady in our database!", 'danger')
            return redirect(url_for("home.index", title="IEEE"))

        # if not the system well continue
        data = newLinkGanaretor(full_name=full_name, email=email)
        hashLink = data["newLink"] # newLinkGanaretor is a function that generate a uniq id and qrcode
        uniqNumber = data["newNumberId"] # get the uniq number
        msg = Message('IEEEEXTREME competition',sender =  ('IEEEEXTREME committee', 'hfibrahim90@gmail.com'),  recipients = [email]) # setup the message sender and recipients and the haer
        # the message main body
        msg.body = '''Id: {}
 Sir : {}
 Peace, mercy and blessings of God
         And yet,
 The IEEE Management is pleased to inform you that you have been selected to attend the Hello Xtreme event
 It will be held in the Hall of the Director of Al-Neelain University on Saturday, 11/9/2021 at 10AM
 All details will be published on the (IEEE Al Neelain University Student Branch) Facebook page.

 * We would like to note that there will be an ongoing competition.  If you wish to participate, you must bring a personal laptop with internet, and thank you for your interest.

 Facebook page link:
 https://www.facebook.com/IEEEANUSB/

* Entry to the hall will be via QR Code which is down below 👇
'''.format(uniqNumber, full_name)

        try: # this block of could catch the error if it happened while sending the email
            with home_page.open_resource(os.path.join(FULL_PATH,"%s.png" % (hashLink)))  as qrcode: # get the qrcode image and attach it with the email
                msg.attach(os.path.join(FULL_PATH,"%s.png" % (hashLink)),"image/png", qrcode.read())
            mail.send(msg) # send the email

            if os.path.exists(os.path.join(FULL_PATH,"%s.png" % (hashLink))): # delete the qrcode after send the email 
                os.remove(os.path.join(FULL_PATH,"%s.png" % (hashLink)))
                print("the file has been remove")
            else: # is the system could not find the image it well print this message
                print("The file does not exist")
        except Exception as e: # If an error occurs while sending the email, it will be redirected to the home page with an error message
            flash("The email was not sent, please check that the security features are enabled in the account settings and that the server supports writing files", 'danger')
            return redirect(url_for("home.index", title="IEEE"))


        # if every thing go well the name and email well save to the database and redirect to the home page 
        newRecord = theAccepted(name=full_name, email=email, hashLink = hashLink, 
        imageNumber = hashLink, uniqNumber = uniqNumber) 
        db.session.add(newRecord) # save the email and the name to the database after the email is send
        db.session.commit() # save the change
        flash("Un E-mail have been send to the provite email!", "success") # show a message that the email hav been send
        return redirect(url_for("home.index", title="IEEE")) # return the main page

    return render_template("form.html", titel="IEEE") # render the main page if the request method is get
