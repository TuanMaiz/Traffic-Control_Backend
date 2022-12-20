import base64
import random 

listPath = ["./assets/cat.jpg", "./assets/cat1.jpg", "./assets/cat2.jpg", "./assets/cat3.jpg"]
def send_frame():
    frame = ''
    str = ''
    i = 0
    while i < 10:
        randomPath = random.choice(listPath)
        print(randomPath)
        # with open(randomPath, "rb")  as image:
        #     str = base64.b64encode(image.read())
        # frame = str.decode('utf-8')
        i = i+1
send_frame()