## Whistleblower-Leak

In this challenge three zip files are concated together to look like one. The one you don't need is in the back and in the front because zip reader always read from the back on and modern ones (like bandizip) from the front, so the secret directory stays hidden. 

The only way to see that there is something interesting is when you use the `unzip -l summer-trip.zip` command to see that there are bytes left.

The Solution command is `binwalk -e summer-trip.zip`, this will get all the three different zip files.