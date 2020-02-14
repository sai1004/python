import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread('messi1.jpg',1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+y, y+h), (0,255,0), 3)

resized = cv2.resize(img , (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('Gray', resized)

cv2.waitKey(0) # if 0 press any key to close window

cv2.destroyAllWindows()

print(type(img))
print(img.shape)