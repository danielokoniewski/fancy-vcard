import logging
from argparse import ArgumentParser
import io
import sys
import qrcode

from .vcard import VCard, VCardVersion

logging.basicConfig(level=logging.INFO)


class Broker:
    _output_version: VCardVersion = VCardVersion.V3
    _output_file_path: str = None

    def make_qr_code(self):
        logging.info(f'making a qr code with version {self._output_version}')
        contact = VCard(self._output_version)
        text = contact.get_text()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.clear()
        qr.add_data(text)
        if self._output_file_path is None:
            self.output_qr_code_text(qr)
        else:
            self.output_qr_code_image(qr)

    def output_qr_code_text(self, qr: qrcode.QRCode):
        logging.info('output to console')
        f = io.StringIO()
        qr.print_ascii(out=f)
        f.seek(0)
        print(f.read())

    def output_qr_code_image(self, qr: qrcode.QRCode):
        logging.info(f'output to file {self._output_file_path}')
        img = qr.make_image()
        img.save(self._output_file_path)


def _argparse() -> ArgumentParser:
    parser = ArgumentParser(
        prog='fancy-vcard-cli',
        description='Shows or creates a vcard qr code.')
    parser.add_argument('-v', '--version',
                        dest="_output_version",
                        help='create vcard version 3 or 4',
                        choices=['3', '4'])
    parser.add_argument('-o', '--output',
                        dest="_output_file_path",
                        help='output file path')
    return parser


def main():
    b = Broker()
    _argparse().parse_args(sys.argv[1:], namespace=b)
    b.make_qr_code()
