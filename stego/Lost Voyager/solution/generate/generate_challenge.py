import wave
import struct
from PIL import Image, ImageDraw
from pysstv.color import Robot36  

def create_space_telemetry_image():
    img = Image.new('RGB', (320, 240), color=(10, 15, 30))
    d = ImageDraw.Draw(img)
    
    d.rectangle([(5, 5), (315, 235)], outline=(0, 255, 255), width=1)
    d.line([(5, 40), (315, 40)], fill=(0, 255, 255), width=1)
    
    d.text((15, 15), "VOYAGER-RECOVERY // DEEP SPACE NETWORK", fill=(0, 255, 255))
    
    d.text((15, 55), "STATUS: MISSION LOSS / AUTONOMOUS BROADCAST", fill=(255, 50, 50))
    d.text((15, 80), "SECTOR: SECTOR-7 // COORDINATES: UNKNOWN", fill=(200, 200, 200))
    d.text((15, 105), "TELEMETRY PAYLOAD ENCRYPTED:", fill=(200, 200, 200))
    
    d.text((15, 140), "FLAG: CLA{V0yag3r_1s_l0st_1n_sp4c3}", fill=(0, 255, 128))
    
    d.text((15, 190), "[EOM] END OF TRANSMISSION [EOM]", fill=(0, 255, 255))
    
    img.save("space_telemetry.png")
    print("[+] 'space_telemetry.png' erfolgreich generiert.")


def convert_to_sstv_audio():
    img = Image.open("space_telemetry.png")
    sstv = Robot36(img, 44100, 16)
    
    output_filename = "lost_voyager_signal.wav"
    
    max_samples = int(37 * 44100)
    
    print(f"[+] Generiere Samples für {max_samples} Frames (Robot36 Mode)...", flush=True)
    
    sample_generator = sstv.gen_samples()
    samples = []
    
    for _ in range(max_samples):
        try:
            samples.append(int(next(sample_generator)))
        except StopIteration:
            break

    print(f"[+] Konvertiere {len(samples)} Samples in Binärformat...", flush=True)
    binary_data = struct.pack(f"<{len(samples)}h", *samples)
    
    print(f"[+] Schreibe WAV-Datei...", flush=True)
    with wave.open(output_filename, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(44100)
        wav.writeframes(binary_data)
                
    print(f"[+] SSTV-Audio erfolgreich exportiert als '{output_filename}'!", flush=True)

if __name__ == "__main__":
    create_space_telemetry_image()
    convert_to_sstv_audio()