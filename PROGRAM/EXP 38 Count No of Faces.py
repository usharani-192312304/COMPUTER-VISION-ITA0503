import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
path = filedialog.askopenfilename()
root.destroy()

image = cv2.imread(path)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face.detectMultiScale(gray, 1.1, 5)

    print("Number of faces:", len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y),
                      (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or unable to read!")
