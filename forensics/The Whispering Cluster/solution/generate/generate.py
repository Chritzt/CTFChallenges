import os
import subprocess

def xor_cipher(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

image_name = "usb_dump.raw"
xor_key = 19
flag = b"CLA{Fl4sh_Dr1v3_Sl4ck_Sp4c3_F0r3ns1cs}"
encrypted_flag = xor_cipher(flag, xor_key)

with open(image_name, "wb") as f:
    f.write(b"\x00" * (1024 * 1024))
subprocess.run(['mkfs.vfat', '-F', '12', '-n', f'XOR-KEY-{xor_key}', image_name])

os.makedirs("mnt_test", exist_ok=True)

uid = os.getuid()

subprocess.run(['sudo', 'mount', '-o', f'loop,uid={uid}', image_name, 'mnt_test'])

try:
    file_path = "mnt_test/vacation.txt"
    with open(file_path, "wb") as f:
        f.write(b"VACATION_PHOTO_METADATA_IGNORE_THIS_LINE")
finally:
    subprocess.run(['sudo', 'umount', 'mnt_test'])
    os.rmdir("mnt_test")

with open(image_name, "r+b") as f:
    content = f.read()
    
    decoy_trigger = b"VACATION_PHOTO_METADATA_IGNORE_THIS_LINE"
    file_pos = content.find(decoy_trigger)
    
    if file_pos == -1:
        print("[-] Fehler: Datei-Inhalt im Image nicht gefunden!")
    else:
        slack_offset = file_pos + len(decoy_trigger)
        
        f.seek(slack_offset)
        f.write(encrypted_flag)
        print(f" Fertig")

print(" Fertig")