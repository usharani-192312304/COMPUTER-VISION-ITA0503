
import cv2
import numpy as np

# Read input image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Image not found")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert into binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply morphological opening
opening = cv2.morphologyEx(
    binary, cv2.MORPH_OPEN, kernel
)

# Apply morphological closing
closing = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel
)

# Display images separately
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Morphological Opening", opening)
cv2.imshow("Morphological Closing", closing)

# Save output images
cv2.imwrite("opening.jpg", opening)
cv2.imwrite("closing.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Opening and Closing completed successfully")
