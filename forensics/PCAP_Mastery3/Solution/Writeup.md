## PCAP_Mastery3

The PCAP in this challenge has a .png transfer over https, so encrypted, however also the sslkeys are exposed so the player can basically just decrypt it.

Just head into wireshark, go to edit -> preferences, then search for Protocols and the SSL protocol and insert the given file as the `(Pre)-Master-Secret log filename`.

Then the traffic is encrypted. Next head to file -> export objects -> http... and select the object that was extracted and save. This is the png with the flag on it.