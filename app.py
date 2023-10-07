from pyzbar.pyzbar import decode
import cv2

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Set the webcam frame width and height
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

# Initialize a flag to indicate if a QR code has been detected
qr_code_detected = False

while not qr_code_detected:
    success, frame = cam.read()

    # Detect QR codes in the frame
    decoded_objects = decode(frame)

    # Process the detected QR codes
    for obj in decoded_objects:
        print(f"QR Code Data: {obj.data.decode('utf-8')}")

        # Set the flag to indicate a QR code has been detected
        qr_code_detected = True

        # Get the location of the QR code within the frame
        rect_points = obj.rect

        # Extract the coordinates of the QR code region
        x, y, w, h = rect_points[0], rect_points[1], rect_points[2], rect_points[3]

        # Crop the QR code region from the frame
        qr_code_cropped = frame[y:y + h, x:x + w]

        # Save the cropped QR code as an image file
        cv2.imwrite("qr_code_detected.png", qr_code_cropped)

        # Face detection using Haar Cascade Classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Process detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the face region from the frame
            face_cropped = frame[y:y + h, x:x + w]

            # Save the cropped face as an image file
            cv2.imwrite("detected_face.png", face_cropped)

    # Display the frame with the detected QR code and face
    cv2.imshow("QR_Code_and_Face_Detector", frame)
    cv2.waitKey(1)

# Release the webcam and close the OpenCV window
cam.release()
cv2.destroyAllWindows()
