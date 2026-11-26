import cv2

# Read image
image = cv2.imread("sample.jpeg")

# Check image
if image is None:
    print("Error: sample.jpg not found")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# Check classifiers
if face_cascade.empty():
    print("Face cascade not loaded")
    exit()

if eye_cascade.empty():
    print("Eye cascade not loaded")
    exit()

if smile_cascade.empty():
    print("Smile cascade not loaded")
    exit()

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

print("Number of faces detected:", len(faces))

# Process each detected face
for (x, y, w, h) in faces:

    # Draw rectangle around face
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        2
    )

    # Extract face region
    face_gray = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (ex, ey, ew, eh) in eyes:

        cv2.rectangle(
            face_color,
            (ex, ey),
            (ex + ew, ey + eh),
            (0, 255, 0),
            2
        )

    # Detect smile
    smiles = smile_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.7,
        minNeighbors=20
    )

    for (sx, sy, sw, sh) in smiles:

        cv2.rectangle(
            face_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 0, 255),
            2
        )

# Display final result
cv2.imshow("Face, Eye and Smile Detection", image)

# Wait for key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
