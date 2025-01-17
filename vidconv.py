import cv2
vidcap = cv2.VideoCapture('VID-20201205-WA0002.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        #src = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        src = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("training-data/regiyan/image"+str(count)+"a.jpg", src)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)