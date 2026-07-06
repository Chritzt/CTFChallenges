#!/usr/bin/env python3
import sys
from scapy.all import rdpcap, IP, ICMP

def extract_flag(pcap_file):
    print(f"[*] Analyzing {pcap_file}...")
    
    try:
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        print(f"[-] Error: File '{pcap_file}' not found.")
        return
    except Exception as e:
        print(f"[-] Error reading PCAP: {e}")
        return

    flag_chars = []

    for pkt in packets:
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 11:
            
            try:
                inner_ip = pkt[ICMP].payload
                
               
                if isinstance(inner_ip, IP):
                    secret_id = inner_ip.id
                    
                    
                    char1 = chr((secret_id >> 8) & 0xFF)
                    char2 = chr(secret_id & 0xFF)
                    
                    flag_chars.append(char1)
                    flag_chars.append(char2)
            except Exception:

                continue

    if not flag_chars:
        print("[-] No covert channel data found in ICMP Type 11 packets.")
        return

    full_string = "".join(flag_chars).strip()
    
    print("[+] Extraction complete!")
    print("--------------------------------------------------")
    print(f"Result: {full_string}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    pcap_name = sys.argv[1] if len(sys.argv) > 1 else "challenge.pcap"
    extract_flag(pcap_name)