from fancy_vcard.vcard import VCard, VCardVersion


def test_v3():
    vcard = VCard(VCardVersion.V3)
    assert vcard.get_text() == """BEGIN:VCARD
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
END:VCARD"""


def test_v4():
    vcard = VCard(VCardVersion.V4)
    assert vcard.get_text() == """BEGIN:VCARD
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
END:VCARD"""  # noqa: B950,E501
