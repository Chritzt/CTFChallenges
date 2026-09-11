import sys

def verify_license():
    print("--- Secure License Verification ---")
    key = input("Enter License Key: ").strip()
    
    if len(key) != 16:
        print("[-] Invalid License Length!")
        return

    targets = [720, 484, 528, 444, 435, 786, 686, 736, 810, 800, 847, 984, 756, 858, 870, 1040]
    
    valid = True
    for i in range(16):
        if (ord(key[i]) * (i + 1)) != targets[i]:
            valid = False
            break

    if valid:
        enc_flag = [25, 22, 27, 33, 56, 35, 109, 105, 57, 106, 62, 105, 5, 56, 110, 49, 105, 40, 5, 55, 110, 41, 46, 105, 40, 39]
        decrypted = "".join([chr(x ^ 0x5A) for x in enc_flag])
        print(f"[+] Access Granted! Flag: {decrypted}")
    else:
        print("[-] Access Denied!")

if __name__ == "__main__":
    verify_license()