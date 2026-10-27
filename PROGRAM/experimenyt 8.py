import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found.")
else:
    colors = ("b", "g", "r")

    for i, color in enumerate(colors):
        histogram = cv2.calcHist(
            [image], [i], None, [256], [0, 256]
        )
        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()
