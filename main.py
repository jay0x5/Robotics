import cv2
import mediapipe as mp
import time
import serial

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)

def write_read(x):
    x = str(x)
    print(x)
    
    time.sleep(1)
    arduino.write(bytes(x,'utf-8'))
    # time.sleep(2)
    data = arduino.readline()
    return data


def mapX( coordX,  in_min,  in_max,  out_min,  out_max):
    
  return (coordX - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

mp_facedetector = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


with mp_facedetector.FaceDetection(min_detection_confidence=0.7) as face_detection:

    while cap.isOpened():

        success, image = cap.read()

        start = time.time()


        # Convert the BGR image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find faces
        results = face_detection.process(image)
        
        # Convert the image color back so it can be displayed
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        if results.detections:
            for id, detection in enumerate(results.detections):
                mp_draw.draw_detection(image, detection)
                # print(id, detection)

                bBox = detection.location_data.relative_bounding_box

                h, w, c = image.shape

                x = bBox.xmin
                y = bBox.ymin
                time.sleep(0.01)
                # Cx = int(x + (x + h))/2
                # Cx = int(Cx)
                # print(Cx)
                mappedX = mapX(x,0,1,190,500)
                XX = int(mappedX)
                
                ard_data = write_read(XX)
                print(ard_data)


                # boundBox = int(bBox.xmin * w), int(bBox.ymin * h), int(bBox.width * w), int(bBox.height * h)

                # cv2.putText(image, f'{int(detection.score[0]*100)}%', (boundBox[0], boundBox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)





        end = time.time()
        totalTime = end - start

        fps = 1 / totalTime
        # print("FPS: ", fps)

        cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

        cv2.imshow('Face Detection', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()