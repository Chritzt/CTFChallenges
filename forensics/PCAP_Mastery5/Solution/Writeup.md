## PCAP_Mastery6

In this challenge, we look at simulated Modbus/TCP traffic, which is an unencrypted industrial OT protocol used to communicate with PLCs (SPS).

The PCAP contains an industrial cyberattack where an attacker overrides internal registers to manipulate physical processes.

To solve this challenge and extract the flag:

Open the PCAP and filter for Modbus packets using Function Code 6 (Write Single Register): modbus.func_code == 6.

Inspect the Raw Data / Register Value of these packets.

The attacker hides the flag piece by piece (two characters per packet) inside the values written to the registers.

