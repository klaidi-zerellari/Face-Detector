import cv2

    # Load some pre-trained data on face frontals from opencv 
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    #Video from Webcam
webcam = cv2.VideoCapture(0)
    #Loop
while True:
    successful_frame_read, frame = webcam.read()



    #Grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

    #Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(frame)

    #Draw Rectangles
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #print(face_coordinates)

    cv2.imshow("Face Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break