import os
import cv2

# Set the output directory
output_dir = "cropped_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all the .jpg and .jpeg files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.jpg') or f.endswith('.jpeg')]

# Loop through all the files
for file in files:
    # Load the image
    image = cv2.imread(file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find the contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    contour = max(contours, key=cv2.contourArea)

    # Get the bounding box for the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Crop the image to the bounding box
    cropped_image = image[y:y+h, x:x+w]

    # Save the cropped image to the output directory
    cv2.imwrite(os.path.join(output_dir, file), cropped_image)
    print("img done")
print("done")