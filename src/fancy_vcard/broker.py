import io

import qrcode

from .vcard import VCard


def main():
    print('hallo from broker')
    make_qr_code()


def make_qr_code():
    contact = VCard()
    text = contact.get_text()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.clear()
    qr.add_data(text)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())
