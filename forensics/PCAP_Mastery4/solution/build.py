from scapy.all import *

flag = "CLA{r0u71ng_l00p5_4r3_c0v3r7_ch4nn3l5}"

if len(flag) % 2 != 0:
    flag += " "

packets = []

router_a = "192.168.100.1"
router_b = "192.168.100.2"
target_ip = "10.0.0.1"

print("[*] Generiere PCAP mit Routing-Schleife...")

for i in range(0, len(flag), 2):
    char1 = flag[i]
    char2 = flag[i+1]
    
    secret_id = (ord(char1) << 8) + ord(char2)
    
    original_packet = IP(src=router_a, dst=target_ip, id=secret_id, ttl=1) / ICMP()
    
    icmp_error = IP(src=router_b, dst=router_a) / ICMP(type=11, code=0) / original_packet
    
    packets.append(icmp_error)
    
    packets.append(IP(src=router_a, dst=router_b)/ICMP(type=8))

wrpcap("challenge.pcap", packets)
print("[+] challenge.pcap erfolgreich erstellt!")