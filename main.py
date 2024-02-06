import cv2

# Read the input image
image = cv2.imread("original_images/zidane.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted = 255 - gray_image

# Apply Gaussian blur to the inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blur = 255 - blur

# Create the sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# Save the sketch image
cv2.imwrite("processed_images/sketch_zidane.png", sketch)

# Display the sketch image
cv2.imshow("Image", sketch)
