## PCAP_Mastery4

In this challenge, you will encounter a large amount of "Time Exceeded" ICMP messages (Type 11). This happens when a packet gets caught in a routing loop and its Time-To-Live (TTL) drops to 0.

The crucial mechanism to understand here is that according to network standards, an ICMP error message encapsulates a copy of the original, failed IP packet inside its payload so the sender knows what went wrong. This embedded part contains a nested (second) IP Header.

To solve the challenge, you need to extract the hidden data from this covert channel:

1. Open the PCAP in Wireshark and filter for icmp.type == 11.

2. Select any "Time Exceeded" packet.

3. In the packet details pane, navigate to:
Internet Control Message Protocol ➔ Internet Protocol Version 4 (The nested/inner header) ➔ Identification.

4. The Identification field holds a 16-bit Hex value (e.g., 0x464c).

5. Convert this Hex value to ASCII to reveal two characters of the flag per packet (e.g., 0x464c ➔ FL).

Repeat this for all error packets (or automate it via tshark / scapy) to piece the full flag together.
