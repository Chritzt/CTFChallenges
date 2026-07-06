from scapy.all import *


def create_modbus_write_packet(trans_id, register, value_16bit):
    mbap = struct.pack(">HHHB", trans_id, 0, 6, 1)
    
    pdu = struct.pack(">BHH", 6, register, value_16bit)
    
    return mbap + pdu

flag = "FLAG{m0dbus_1ndus7r14l_s4b074g3_07}"
if len(flag) % 2 != 0:
    flag += " "

packets = []
start_register = 1000
base_ip = "192.168.1.50" 
attacker_ip = "192.168.1.210"

print("[*] Generiere Modbus-Angriff-PCAP...")


for i in range(10):
    mbap = struct.pack(">HHHB", i, 0, 6, 1)
    pdu = struct.pack(">BHH", 3, 100, 2) 
    pkt = IP(src=attacker_ip, dst=base_ip)/TCP(sport=34567+i, dport=502)/Raw(load=mbap+pdu)
    packets.append(pkt)

for i in range(0, len(flag), 2):
    char1 = flag[i]
    char2 = flag[i+1]
    val_16bit = (ord(char1) << 8) + ord(char2)
    
    current_reg = start_register + (i // 2)
    modbus_data = create_modbus_write_packet(100 + i, current_reg, val_16bit)
    
    pkt = IP(src=attacker_ip, dst=base_ip)/TCP(sport=50000+i, dport=502)/Raw(load=modbus_data)
    packets.append(pkt)

wrpcap("challenge.pcap", packets)
print("[+] challenge.pcap wurde erstellt!")