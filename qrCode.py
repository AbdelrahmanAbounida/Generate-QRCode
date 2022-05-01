import binascii
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

########################### Serial Number ######################################

inpt = "10000000000000000000000012345"

########################### Create Qr Code ######################################

def createQR():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=0
    )

    qr.add_data(inpt)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


########################### Design the final Label ######################################

def designLabel():
    img_bg = Image.new('1', (304, 135), 1)  # white background image - width: 304, height:135
    texts = ['Text1', 'Text2', 'Text3', 'Text4']  ## List of strings
    draw = ImageDraw.Draw(img_bg)
    font = ImageFont.truetype('arialbd.ttf',
                              18)  # you can choose font name from windows fonts or download a ttf file from google fonts and use it
    draw.text((0, 107), inpt, 0, font=font)
    font = ImageFont.truetype('arialbd.ttf', 18)
    yspace = 25  # difference in ypositoin between each string
    xspace = 107  # xposition of the list of strings
    draw.text((xspace, 5), texts[0], 0, font=font)
    draw.text((xspace, 5 + yspace), texts[1], 0, font=font)
    draw.text((xspace, 5 + yspace * 2), texts[2], 0, font=font)
    draw.text((xspace, 5 + yspace * 3), texts[3], 0, font=font)
    return img_bg


########################### Convert the generated pixel values (0,255) >> (1,0) ######################################
def conv_list(l):
    a = ''
    for i in l:
        if i == 0:
            a = a + '1'
        else:
            a = a + '0'
    return a


########################### Generate the Binary file ######################################
def createBinary(imgname):
    im = Image.open(imgname)
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    newFile = open("newHex", "wb")  #### name the binary file
    for k in pixels:
        c = conv_list(k)
        hstr = '%0*X' % ((len(c) + 3) // 4, int(c, 2))
        newFile.write(binascii.unhexlify(''.join(hstr.split())))


if __name__ == '__main__':
    pos = (0, 5)  # position of the QR Code
    qrCode = createQR()
    label = designLabel()
    label.paste(qrCode, pos)
    labelname = 'newsample.png'  # labellName
    label.save(labelname, format='png')
    createBinary(labelname)
