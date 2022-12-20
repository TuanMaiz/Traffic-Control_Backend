import socketio
import asyncio
import time
import base64
import random
import cv2
sio = socketio.AsyncClient()


# video = cv.VideoCapture('./assets/video.mp4')
listPath = ["./assets/cat.jpg", "./assets/cat1.jpg", "./assets/cat2.jpg", "./assets/cat3.jpg", "./assets/cat4.jpg", "./assets/cat5.jpg", "./assets/cat6.jpg", "./assets/cat7.jpg", "./assets/cat8.jpg"]

@sio.event
async def connect():
    print('connection established')

# @sio.event
# async def my_message(data):
#     print('message received with ', data)
#     await sio.emit('on-chat', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')
# @sio.event
# async def send_msg(): # gonna be the send_frame func
#     await sio.emit('on-chat', {'message': 'Hi i am ' + sio.sid})

@sio.event
async def send_frame():
    for i in range(10):
        frame = ''
        str = ''
        time.sleep(6)
        randomPath = random.choice(listPath)
        print(randomPath)
        with open(randomPath, "rb")  as image:
            str = base64.b64encode(image.read())
        frame = str.decode('utf-8')
        await sio.emit('send-frame', {'frame': frame})
        i = i+1
@sio.event
async def send_frame1():
    for i in range(20):
        # time.sleep(3)
        randomPath = random.choice(listPath)
        print(randomPath)
        with open(randomPath, "rb")  as image:
            frame = base64.encodebytes(image.read()).decode('utf-8')
            await sio.emit('send-frame', {'frame': frame})
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        i = i+1



async def main():
    await sio.connect('http://localhost:3001')
    await send_frame1()
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())