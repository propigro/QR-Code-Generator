import requests
from PIL import Image
from io import BytesIO

def rmd(num, text):
    if num == 1:
        return {
            "data": text,
            "config": {
                "body": "rounded-pointed",
                "eye": "frame14",
                "eyeBall": "ball16",
                "erf1": [],
                "erf2": ["fh"],
                "erf3": ["fv"],
                "brf1": [],
                "brf2": ["fh"],
                "brf3": ["fv"],
                "bodyColor": "#5C8B29",
                "bgColor": "#FFFFFF",
                "eye1Color": "#3F6B2B",
                "eye2Color": "#3F6B2B",
                "eye3Color": "#3F6B2B",
                "eyeBall1Color": "#60A541",
                "eyeBall2Color": "#60A541",
                "eyeBall3Color": "#60A541",
                "gradientColor1": "#5C8B29",
                "gradientColor2": "#25492F",
                "gradientType": "radial",
                "gradientOnEyes": False,
                "logo": ""
            },
            "size": 1024,
            "download": True,
            "file": "png"
        }
    if num == 2:
        return {
            'data': text,
            'config': {
                'body': 'japnese',
                'eye': 'frame6',
                'eyeBall': 'ball6',
                'gradientColor1': '#3d5397',
                'gradientColor2': '#83502e',
                'gradientType': 'radial',
                'gradientOnEyes': True,
                'brf2': ['fh'],
                'brf3': ['fh'],
                'erf2': ['fv'],
                'erf3': ['fv']
            },
            'size': 1024,
            'download': True,
            'file': 'png'
        }
    if num == 3:
        return {
            "data": text,
            "config": {
                "body": "circular",
                "eye": "frame1",
                "eyeBall": "ball8",
                "erf1": ['fh'],
                "erf3": ['fv', 'fh'],
                "brf1": ['fv', 'fv'],
                "gradientColor1": "#ff0000",
                "gradientColor2": "#40c219",
                "gradientType": "linear",
                "gradientOnEyes": True,
            },
            "size": 1024,
            "download": True,
            "file": "png"
        }
    if num == 4:
        return {
            'data': text,
            'config': {
                'body': 'rounded-pointed',
                'eye': 'frame2',
                'eyeBall': 'ball2',
                'gradientColor1': '#ff931c',
                'gradientColor2': '#dc143c',
                'gradientType': 'radial',
                'gradientOnEyes': True,
                'brf3': ['fv', 'fv'],
                'brf2': ['fv', 'fh'],
                'erf2': ['fv'],
                'brf1': ['fv'],
                'erf3': ['fv'],
                'erf1': ['fv', 'fv']
            },
            'size': 1024,
            'download': True,
            'file': 'png'
        }
text = "QR Code yasash!"
width = len(text) + 4 
top = "╔" + "═" * (width - 2) + "╗"
middle = "║ " + text + " ║"
bottom = "╚" + "═" * (width - 2) + "╝"
print(top)
print(middle)
print(bottom)


def qr_code(num, text):
    api_url = "https://api.qrcode-monkey.com/qr/custom"
    js = rmd(num, text)
    response = requests.post(url=api_url, json=js)
    image_url = f"https:{response.json()['imageUrl']}"
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    img.show()
    print(f"Sizning QR Code ingiz tayyor! Uning linki: {image_url}\n")

while True:
    text = input("QR Code uchun matn kiriting: ")
    while True:
        num = input("QR Code ni dizaynini raqamini kiriting (1 - 4 ta dizayn mavjud): ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 4:
                qr_code(num, text)  
                break  
            else:
                print("Raqam 1 dan 4 gacha bo'lishi kerak!")
        else:
            print("Iltimos, faqat raqam kiriting!")
    
    