import os
import qrcode

def generate_unique_filename(base_filename, folder):
    index = 1
    while True:
        new_filename = f"{base_filename}_{index}.png"
        full_path = os.path.join(folder, new_filename)
        if not os.path.exists(full_path):
            return new_filename, full_path
        index += 1

def main():
    data = input("Enter the data you want to encode in the QR code: ")
    output_folder = "qr_codes"
    file_name = 'qr'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    unique_filename, full_path = generate_unique_filename(file_name, output_folder)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=120,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save(full_path)
    print(f"QR code generated and saved as '{unique_filename}' in '{output_folder}'")

if __name__ == "__main__":
    main()
