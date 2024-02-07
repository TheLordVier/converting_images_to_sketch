import os
import cv2


def convert_images(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    converted_images = []  # list of converted images

    # Iterate through images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Read the input image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

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
            output_path = os.path.join(output_folder, f"sketch_{os.path.splitext(filename)[0]}.png")
            cv2.imwrite(output_path, sketch)

            # Add the filename to the list of converted images
            converted_images.append(filename)

    return converted_images


if __name__ == '__main__':
    input_folder = "original_images"
    output_folder = "processed_images"
    converted_images = convert_images(input_folder, output_folder)

    # Print a message indicating the completion of image conversion
    print("Image conversion completed.")

    # Print the list of converted images
    print("Converted images:")
    for image_name in converted_images:
        print(image_name)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
