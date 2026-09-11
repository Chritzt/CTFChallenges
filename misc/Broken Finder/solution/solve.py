import cv2
import numpy as np

def solve():
    img = cv2.imread("broken_qr.png")
    if img is None:
        print("[!] Konnte 'broken_qr.png' nicht finden.")
        return

    def draw_finder_pattern(img, x, y):
        cv2.rectangle(img, (x, y), (x + 70, y + 70), (0, 0, 0), -1)
        cv2.rectangle(img, (x + 10, y + 10), (x + 60, y + 60), (255, 255, 255), -1)
        cv2.rectangle(img, (x + 20, y + 20), (x + 50, y + 50), (0, 0, 0), -1)

    box = 10
    border_px = 4 * box
    width = img.shape[1]
    height = img.shape[0]

    draw_finder_pattern(img, border_px, border_px)
    right_start = width - border_px - 7 * box
    draw_finder_pattern(img, right_start, border_px)
    bottom_start = height - border_px - 7 * box
    draw_finder_pattern(img, border_px, bottom_start)

    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        print(f"[+] Flag gefunden: {data}")
    else:
        print("[!] Konnte den QR-Code nicht decodieren.")

if __name__ == "__main__":
    solve()