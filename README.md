# run

1 command to show the(m all!!!) qr code 
```commandline
fancy-vcard-cli
```

# dev
## setup 
```commandline
poetry install
```
## check
```commandline
poetry run flake8
poetry run coverage run -m pytest && \
poetry run coverage report -m
```

## changes
```commandline
# init
poetry new --src fancy-vcard
# add dependency
poetry add qrcode
```


build with [poetry](https://python-poetry.org/docs/cli/)