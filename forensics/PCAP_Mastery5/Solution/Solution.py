#!/usr/bin/env python3
import sys
import struct
from scapy.all import rdpcap, TCP, Raw

def solve_modbus(pcap_file):
    print(f"[*] Analyzing {pcap_file} for Modbus sabotage...")
    
    try:
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        print(f"[-] Error: File '{pcap_file}' not found.")
        return

    flag_bytes = bytearray()

    for pkt in packets:
        if pkt.haslayer(TCP) and pkt[TCP].dport == 502 and pkt.haslayer(Raw):
            payload = pkt[Raw].load
            
            
            if len(payload) >= 12:

                _, _, length, unit_id = struct.unpack_bytes = struct.unpack(">HHHB", payload[:7])

                function_code = payload[7]
                

                if function_code == 6:

                    register, value_16bit = struct.unpack(">HH", payload[8:12])
                    
                    
                    if register >= 1000:

                        char1 = (value_16bit >> 8) & 0xFF
                        char2 = value_16bit & 0xFF
                        
                        flag_bytes.append(char1)
                        flag_bytes.append(char2)

    if not flag_bytes:
        print("[-] No rogue Modbus register writes found.")
        return

    flag = flag_bytes.decode('utf-8', errors='ignore').strip()
    
    print("[+] Flag successfully extracted from PLC registers!")
    print("--------------------------------------------------")
    print(f"Result: {flag}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    pcap_name = sys.argv[1] if len(sys.argv) > 1 else "challenge.pcap"
    solve_modbus(pcap_name)