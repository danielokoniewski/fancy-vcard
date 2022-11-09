from enum import Enum


class VCardVersion(Enum):
    V3 = 3
    V4 = 4


class VCard:
    """
    https://www.rfc-editor.org/rfc/rfc6350

    """
    _version: VCardVersion

    text_content_v3 = """
BEGIN:VCARD
VERSION:3.0
N:Mustermann;Erika;;Dr.;
FN:Dr. Erika Mustermann
ORG:Wikimedia
ROLE:Kommunikation
TITLE:Redaktion & Gestaltung
PHOTO;VALUE=URL;TYPE=JPEG:http://commons.wikimedia.org/wiki/File:Erika_Mustermann_2010.jpg
TEL;TYPE=WORK,VOICE:+49 221 9999123
TEL;TYPE=HOME,VOICE:+49 221 1234567
ADR;TYPE=HOME:;;Heidestraße 17;Köln;;51147;Germany
EMAIL;TYPE=PREF,INTERNET:erika@mustermann.de
URL:http://de.wikipedia.org/
REV:2014-03-01T22:11:10Z
END:VCARD
"""

    text_content_v4 = """
BEGIN:VCARD
VERSION:4.0
N:Mustermann;Erika;;Dr.;
FN:Dr. Erika Mustermann
ORG:Wikimedia
ROLE:Kommunikation
TITLE:Redaktion & Gestaltung
PHOTO;MEDIATYPE=image/jpeg:http://commons.wikimedia.org/wiki/File:Erika_Mustermann_2010.jpg
TEL;TYPE=work,voice;VALUE=uri:tel:+49-221-9999123
TEL;TYPE=home,voice;VALUE=uri:tel:+49-221-1234567
ADR;TYPE=home;LABEL="Heidestraße 17\n51147 Köln\nDeutschland":;;Heidestraße 17;Köln;;51147;Germany
EMAIL:erika@mustermann.de
REV:20140301T221110Z
END:VCARD
"""

    def __init__(self, version: VCardVersion = VCardVersion.V3):
        self._version = version

    def get_text(self) -> str:
        return self.text_content_v3 if self._version == VCardVersion.V3 else self.text_content_v4
