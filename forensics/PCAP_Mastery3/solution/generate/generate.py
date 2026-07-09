from scapy.all import wrpcap, Ether, IP, UDP, DNS, DNSQR
import base64
import time

def create_dns_challenge(flag, pcap_output):
    print(f"[+] Starte Generierung für Flagge: {flag}")
    
    flag_bytes = flag.encode('utf-8')
    b64_flag = base64.b64encode(flag_bytes).decode('utf-8')
    print(f"[+] Flagge zu Base64 kodiert: {b64_flag}")
    

    chunk_size = 8
    chunks = [b64_flag[i:i+chunk_size] for i in range(0, len(b64_flag), chunk_size)]
    
    packets = []
    
    src_ip = "192.168.122.42"  
    dst_ip = "8.8.8.8"         
    sport = 53535
    dport = 53                 
    
    print("[+] Baue DNS-Pakete...")
    
    for index, chunk in enumerate(chunks):
        query_domain = f"{chunk}.google.com"
        
        pkt = (Ether() / 
               IP(src=src_ip, dst=dst_ip) / 
               UDP(sport=sport, dport=dport) / 
               DNS(rd=1, qd=DNSQR(qname=query_domain, qtype="A")))
        
        packets.append(pkt)
        print(f"  -> Paket {index} hinzugefügt: {query_domain}")
    
    wrpcap(pcap_output, packets)
    print(f"\n[=== ERFOLG ===]\n[->] '{pcap_output}' wurde fehlerfrei generiert!")

if __name__ == "__main__":
    MY_FLAG = "CLA{dn5_3xf1l7r4710n_15_5734l7h_b01}"
    create_dns_challenge(MY_FLAG, "dns_challenge.pcap")