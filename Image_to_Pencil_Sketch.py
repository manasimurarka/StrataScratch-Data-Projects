import cv2
import os

# Ask user for input image path
image_path = input("Enter the full path of the image: ")

# Check if image exists
if not os.path.isfile(image_path):
    print("Error: Image file not found.")
    exit()

# Ask user for output folder
output_folder = input("Enter the folder where you want to save the sketch: ")

output_filename = input("Enter the name of the file(with .png at end) for the output sketch: ")

# Check if folder exists
if not os.path.isdir(output_folder):
    print("Error: Output folder does not exist.")
    exit()

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not read the image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert grayscale image
inverted = 255 - gray

# Blur inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blur = 255 - blur

# Create pencil sketch
sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# Create output file path
output_path = os.path.join(output_folder, output_filename)

# Save sketch
cv2.imwrite(output_path, sketch)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Sketch saved successfully at: {output_path}")
