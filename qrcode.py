from pyzbar.pyzbar import decode
from PIL import Image  
import cv2
import numpy as np


cv2.namedWindow("Python Qr-Code Detection")
cap = cv2.VideoCapture(0)

while True:
    ret, im = cap.read()
    if not ret:
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Decode the QR code
    decoded_objects = decode(gray)

    for obj in decoded_objects:
        print('decoded', obj.type, 'symbol', '"%s"' % obj.data.decode('utf-8'))
        points = obj.polygon

        # If the points form a quadrilateral
        if len(points) == 4:
            topLeft, topRight, bottomRight, bottomLeft = points
            cv2.line(im, topLeft, topRight, (255, 0, 0), 2)
            cv2.line(im, topRight, bottomRight, (255, 0, 0), 2)
            cv2.line(im, bottomRight, bottomLeft, (255, 0, 0), 2)
            cv2.line(im, bottomLeft, topLeft, (255, 0, 0), 2)

            # 2D image points
            image_points = np.array([
                (int((topLeft.x + topRight.x) / 2), int((topLeft.y + bottomLeft.y) / 2)),  # Nose
                (topLeft.x, topLeft.y),  # Left eye left corner
                (topRight.x, topRight.y),  # Right eye right corner
                (bottomLeft.x, bottomLeft.y),  # Left Mouth corner
                (bottomRight.x, bottomRight.y),  # Right mouth corner
                (int((topLeft.x + bottomRight.x) / 2), int((topLeft.y + bottomRight.y) / 2))  # Additional point
            ], dtype="double")

            # 3D model points
            model_points = np.array([
                (0.0, 0.0, 0.0),  # Nose
                (-225.0, 170.0, -135.0),  # Left eye left corner
                (225.0, 170.0, -135.0),  # Right eye right corner
                (-150.0, -150.0, -125.0),  # Left Mouth corner
                (150.0, -150.0, -125.0),  # Right mouth corner
                (0.0, 0.0, -100.0)  # Additional point
            ])

            # Camera internals
            focal_length = im.shape[1]
            center = (im.shape[1] / 2, im.shape[0] / 2)
            camera_matrix = np.array(
                [[focal_length, 0, center[0]],
                 [0, focal_length, center[1]],
                 [0, 0, 1]], dtype="double"
            )

            dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
            (success, rotation_vector, translation_vector) = cv2.solvePnP(
                model_points, image_points, camera_matrix, dist_coeffs)

            (nose_end_point2D, jacobian) = cv2.projectPoints(
                np.array([(0.0, 0.0, 100.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

            for p in image_points:
                cv2.circle(im, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)

            p1 = (int(image_points[0][0]), int(image_points[0][1]))
            p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

            # Draw lines
            cv2.line(im, (bottomLeft.x, bottomLeft.y), p2, (255, 0, 0), 2)
            cv2.line(im, (topLeft.x, topLeft.y), p2, (255, 0, 0), 2)
            cv2.line(im, (bottomRight.x, bottomRight.y), p2, (255, 0, 0), 2)
            cv2.line(im, (topRight.x, topRight.y), p2, (255, 0, 0), 2)

    # Display image
    cv2.imshow("Output", im)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
