## Broken Finder

When opening the provided broken_qr.png image, we immediately notice that the three corner alignment squares (finder patterns) are completely whited out. Standard smartphone cameras and QR readers fail to parse the image because these patterns are strictly required for orientation and scaling.

Looking closer at the data matrix in the center, the pixels are fully intact. Furthermore, the QR code was generated with a high error-correction level (ERROR_CORRECT_H), meaning it can withstand substantial damage. The only missing part is the geometry and detection markers.

We can write a Python script using OpenCV (cv2) to manually redraw the standard 7x7 finder patterns onto the top-left, top-right, and bottom-left corners over the white blocks.

Once the patterns are restored, passing the modified image to OpenCV's QRCodeDetector instantly decodes the payload and reveals the flag.