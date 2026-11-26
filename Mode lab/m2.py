import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Image not found")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Green color threshold
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Create binary mask
mask = cv2.inRange(hsv, lower_green, upper_green)

# Extract foreground
foreground = cv2.bitwise_and(image, image, mask=mask)

# Display mask and extracted object
cv2.imshow("Original Image", image)
cv2.imshow("Binary Mask", mask)
cv2.imshow("Extracted Foreground", foreground)

# Save final result
cv2.imwrite("foreground_result.jpg", foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Foreground image saved successfully.")
