#!/usr/bin/env python
# -*- CODING=UTF-8-*-

import requests
from io import BytesIO
from PIL import Image

url = 'https://open.weixin.qq.com/connect/qrcode/071m4FLlnyMhxl2q'

res = requests.get(url)

img = Image.open(BytesIO(res.content))

img.show()