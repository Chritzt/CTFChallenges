from scapy.all import IP, ICMP, wrpcap


flag = "FLAG{ttl_c4n_4l50_h1d3_s3cr3t5}"

pcap_packets = []

print("Generiere ICMP-Pakete...")
for char in flag:
    ascii_value = ord(char) 
    
    packet = IP(src="10.0.0.5", dst="10.0.0.10", ttl=ascii_value) / ICMP(type=8)
    pcap_packets.append(packet)

wrpcap("challenge_icmp.pcap", pcap_packets)
print("Datei 'challenge_icmp.pcap' erfolgreich erstellt!")