import cv2

# Read image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel gradients
gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert gradients to displayable images
gradient_x = cv2.convertScaleAbs(gradient_x)
gradient_y = cv2.convertScaleAbs(gradient_y)

# Combined gradient magnitude
magnitude = cv2.magnitude(
    gradient_x.astype("float32"),
    gradient_y.astype("float32")
)
magnitude = cv2.convertScaleAbs(magnitude)

# Display results separately
cv2.imshow("Original Image", image)
cv2.imshow("Horizontal Edges - Sobel X", gradient_x)
cv2.imshow("Vertical Edges - Sobel Y", gradient_y)
cv2.imshow("Combined Edge Magnitude", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
