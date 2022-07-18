# imports
import cv2

# make a  list for images
images = ['../Assets/harry.jpg','../Assets/harry2.jpg','../Assets/harry3.jpg','../Assets/harry4.jpeg','../Assets/harry5.png','../Assets/harry6.jpg','../Assets/harry7.jpg']

# loop for importing images from the list
for i in images:
    image = cv2.imread(i)

    # convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # detect multiscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # loop
    for (x,y,w,h) in faces:
        # detect face
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        # detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # show img with detection
    cv2.imshow('image',image)

    # wait for user to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()