import cv2

def capture(date,id):
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    cv2.imwrite(f'captures/{date}_{id}.png', frame)
    vid.release()



capture('20220211','123')
capture('20220211','456')

