import qrcode
from PIL import Image
import image

qr = qrcode.QRCode(
    version = 15,
    box_size=10,
    border=1
)
data = "You scanned me? \ncute."
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
