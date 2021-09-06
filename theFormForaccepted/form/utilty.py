# the import part
import uuid # import the hash lib.
import os # import python system lib.
import qrcode # import the qrcode generater
from PIL import Image # import python images generater
from models import theAccepted
from theFormForaccepted import PROJECT_ROOT # import the project path


FULL_PATH = os.path.join(PROJECT_ROOT, 'theFormForaccepted/form/qrCode_images') # make the full path to the qrcode images folder
startNumber = 0 # the number which well start fron it the number id 

qr = qrcode.QRCode( # setup the qrcode setting 
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

'''

    LOGIC -> the functions blow well generate a uniq qrcode image and a link which well save to the database
    We can perform the verification process by scanning the QR code and searching the database for a match
    with the code information and adding the condition that this code has not been scanned before

    With the addition of a number to be verified in the event that a scan of the qrcode code fails for any reason

'''

def newLinkGanaretor(full_name, email): # this function generate a uniq link and qrcode and return the uniq link, number using the name and the email
    newLink = uuid.uuid1().hex # generate a uniq link
    newNumberId = startNumber + 1 # generate a uniq number id
    qr.add_data({"Name" : full_name,
    "E-mai" : email,
    "Link" :newLink,
    "UniqID" : newNumberId }) # add the data(name, email) to the qrcode image
    qr.make(fit=True) # make the qrcode image fit well
    img = qr.make_image(fill_color="white", back_color="black").convert('RGB') # set the background and front color for the qrcode image and convert it to RGB type
    logo_display = Image.open(os.path.join(PROJECT_ROOT, 'theFormForaccepted/static/ieeeLogo.png')) # get the IEEE logo image 
    logo_display.thumbnail((100, 100)) # add the logo image to the qrcode image
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2) # center the IEEE logo image 
    img.paste(logo_display, logo_pos) # add all it togather
    # print(PROJECT_ROOT)
    img.save(os.path.join(FULL_PATH,"%s.png" % (newLink))) # save the new qrcode image withe the logo to the image folder
    data = {"newLink" : newLink, "newNumberId" : newNumberId}
    return data  # return the uniq hash link


