import cv2
import numpy as np

# Function to decrypt message from an image
def decrypt_message(img_path, password):
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Image not found.")
        return ""

    c = {i: chr(i) for i in range(256)}
    
    message = ""
    index = 0
    msg_length = None  # Initialize to prevent UnboundLocalError
    h, w, _ = img.shape

    for i in range(h):
        for j in range(w):
            for k in range(3):  # Iterate over RGB channels
                char = c[img[i, j, k]]
                message += char
                index += 1

                # Extract the message length from the first 3 characters
                if index == 3:
                    try:
                        msg_length = int(message)  # Extract length from first 3 chars
                        message = ""  # Reset message to store actual text
                        print(f"Detected message length: {msg_length}")  # Debugging line
                    except ValueError:
                        print("Error: Invalid message format in image.")
                        return ""

                # Stop reading after retrieving full message
                if msg_length is not None and len(message) == msg_length:
                    return message

    print("Error: Message not found or corrupted.")
    return ""

# Main execution
if __name__ == "__main__":
    img_path = "encryptedImage.png"  # Use PNG format for lossless decryption
    password = input("Enter passcode for Decryption: ")

    decrypted_msg = decrypt_message(img_path, password)
    print("Decrypted message:", decrypted_msg)
