import uuid
import os
import qrcode
from PIL import Image
from models import theAccepted
from theFormForaccepted import mail, Message, PROJECT_ROOT


FULL_PATH = os.path.join(PROJECT_ROOT, 'theFormForaccepted/form/qrCode_images')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)


def newLinkGanaretor(full_name, email):
    newLink = uuid.uuid1().hex
    qr.add_data({"Name" : full_name,
    "E-mai" : email,
    "Link" :newLink })
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    logo_display = Image.open('theFormForaccepted/static/ieeeLogo.png')
    logo_display.thumbnail((200, 100))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)
    img.save(os.path.join(FULL_PATH,"%s.png" % (newLink)))
    return newLink
