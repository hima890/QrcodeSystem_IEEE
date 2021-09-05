from flask import Blueprint, app, redirect, render_template, url_for, request, jsonify, flash
from sqlalchemy.orm import query
from theFormForaccepted import db
from models import theAccepted
from theFormForaccepted.form.utilty import newLinkGanaretor
from theFormForaccepted import mail, Message, create_app as app
import os


home_page = Blueprint('home', __name__, static_folder='static', template_folder='templates')

@home_page.route("/", methods=["POST", "GET"])
@home_page.route("/home", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        query_check = theAccepted.query.filter_by(email=email).first()
        if query_check:
            return render_template("500.html", title="Error")

        hashLink = newLinkGanaretor(full_name=full_name, email=email)
        newRecord = theAccepted(name=full_name, email=email, hashLink = hashLink, 
        imageNumber = hashLink)
        db.session.add(newRecord)
        db.session.commit()


        msg = Message('IEEEEXTREME competition',sender =  ('IEEEEXTREME committee', 'hfibrahim90@gmail.com'),  recipients = [email])
        msg.body = '''And yet,
        The IEEE Management is pleased to inform you that you have been selected to attend the IEEEEXTREME competition
        Details will be posted on (Page Name) Facebook page

        Facebook page link:

        We would like to note that you must bring a personal laptop with internet, and there will be a small competition to attend, and entry to the hall will be via QR Code'''
        qrcode_path = "qrCode_images/%s.png" % (hashLink)
        with home_page.open_resource(qrcode_path)  as qrcode:
            msg.attach(qrcode_path,"image/png", qrcode.read())
        mail.send(msg)
        if os.path.exists("theFormForaccepted/form/qrCode_images/%s.png" % (hashLink)):
            os.remove("theFormForaccepted/form/qrCode_images/%s.png" % (hashLink))
            print("the file has been remove")
        else:
            print("The file does not exist")


    return render_template("form.html", titel="IEEE")
