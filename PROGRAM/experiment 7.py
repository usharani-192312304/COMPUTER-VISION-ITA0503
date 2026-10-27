
import cv2

video_path = r"C:\Users\usha reddy\OneDrive\Desktop\computer vision\exp 7\videeo.webm"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video. Check the file.")
else:
    print("Video opened successfully!")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("My Video", frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
