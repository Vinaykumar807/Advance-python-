import cv2
import tkinter as tk
from tkinter import filedialog

# Create a file selection window
root = tk.Tk()
root.withdraw()

# Ask the user to select an image
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("No image selected or unable to read the image.")
    exit()

# Flip the image
# 1  = Horizontal flip
# 0  = Vertical flip
# -1 = Both horizontal and vertical
flipped_image = cv2.flip(image, 1)

# Display original and flipped image
cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)

# Save the flipped image
cv2.imwrite("flipped_image.jpg", flipped_image)

print("Flipped image saved as flipped_image.jpg")

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()