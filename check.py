import os
import cv2
import qrcode

def main():
    input_folder = "qr_codes"  # Change this to your folder containing QR code images

    if not os.path.exists(input_folder):
        print(f"The '{input_folder}' folder does not exist.")
        return

    qr_decoder = cv2.QRCodeDetector()

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            decoded_data, _ = qr_decoder.detectAndDecode(image)
            if decoded_data:
                print(f"QR code in '{filename}' contains: {decoded_data}")
            else:
                print(f"'{filename}' does not contain a valid QR code.")

if __name__ == "__main__":
    main()

