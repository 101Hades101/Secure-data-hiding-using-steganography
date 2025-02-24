import cv2
import numpy as np
import os

# Function to encrypt message into an image
def encrypt_message(img_path, output_path, msg, password):
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Image not found.")
        return
    
    # Ensure the output image is removed before writing a new one
    if os.path.exists(output_path):
        os.remove(output_path)

    msg = f"{len(msg):03d}{msg}"  # Prefix message with length (3 digits)

    d = {chr(i): i for i in range(256)}
    index = 0
    h, w, _ = img.shape

    for i in range(h):
        for j in range(w):
            for k in range(3):  # Iterate over RGB channels
                if index < len(msg):
                    img[i, j, k] = d[msg[index]]
                    index += 1
                else:
                    break  # Stop writing once the message is fully embedded

    # Save in PNG format to prevent compression issues
    cv2.imwrite(output_path, img)
    print(f"Message encrypted and saved to {output_path}")

# Main execution
if __name__ == "__main__":
    img_path = "pictureSpidey.jpg"
    output_path = "encryptedImage.png"  # Use PNG format for lossless storage
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    encrypt_message(img_path, output_path, msg, password)
