import qrcode
from PIL import Image

def generate_broken_qr():
    flag = "CLA{qr_c0d3_r3p41r_m4st3r}"
    
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(flag)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    pixels = img.load()
    width, height = img.size
    
    box = 10
    border_px = 4 * box
    
    for x in range(border_px, border_px + 7 * box):
        for y in range(border_px, border_px + 7 * box):
            pixels[x, y] = (255, 255, 255)
            
    right_start = width - border_px - 7 * box
    for x in range(right_start, right_start + 7 * box):
        for y in range(border_px, border_px + 7 * box):
            pixels[x, y] = (255, 255, 255)

    bottom_start = height - border_px - 7 * box
    for x in range(border_px, border_px + 7 * box):
        for y in range(bottom_start, bottom_start + 7 * box):
            pixels[x, y] = (255, 255, 255)


    output_filename = "broken_qr.png"
    img.save(output_filename)
    print(f"[+] Challenge-Bild erfolgreich als '{output_filename}' erstellt!")

if __name__ == "__main__":
    generate_broken_qr()