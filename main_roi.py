import pathlib
import cv2
import torch
import numpy as np

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap = cv2.VideoCapture('roi_fast.mp4')

 # For saving the output video to local folder
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output_roi.avi', fourcc, 20.0, (1020, 500))

def points(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', points)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    # getting the bounding box coordinates of the objects
    for index, row in results.pandas().xyxy[0].iterrows():
        x = int(row['xmin'])
        y = int(row['ymin'])
        w = int(row['xmax'])
        h = int(row['ymax'])
        nm = str(row['name'])

        # coordinates for the ROI
        area = [(120, 183), (2, 245), (2, 478), (850, 478), (850, 200)]
        mask = np.zeros_like(frame)

        color = (0, 0, 255)
        opacity = 0.2
        text_position = (15, 45)

        cv2.fillPoly(mask, [np.array(area, np.int32)], color)
        cv2.polylines(frame, [np.array(area, np.int32)], True, color, 1)

        # checks if the 'person' or 'car' class enters the ROI
        if nm == 'person' or nm == 'car':
            if nm == 'person':
                cv2. rectangle(frame, (x, y), (w, h), (173, 216, 230), 2)
            else:
                cv2.rectangle(frame, (x, y), (w, h), (255, 255, 0), 2)

            # function which checks if the point is within the ROI
            result = cv2.pointPolygonTest(np.array(area, np.int32), (int(w), int(h)), False)
            print(result)
            if result == 1.0:
                # gives a coloured layer if there is invasion into the ROI
                frame = cv2.addWeighted(frame, 1, mask, opacity, 0)

                cv2.rectangle(frame, (8, 10), (325, 60), (0, 0, 0), -1)
                cv2.putText(frame, 'Suspicious Activity!', text_position, cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

    frame = cv2.resize(frame, (1020, 500))
    # out.write(frame)
    cv2.imshow('FRAME', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()






