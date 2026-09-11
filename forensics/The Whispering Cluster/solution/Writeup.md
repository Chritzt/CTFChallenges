## The Whispering Clusters

### Step 1: File System Metadata Analysis
First, we analyze the metadata of the raw disk image using `fsstat` (from The Sleuth Kit) to understand the filesystem structure and look for initial anomalies.

```bash
fsstat usb_dump.

```

In the output, the Volume Label stands out immediately:
* Volume Label (Boot Sector): XOR_KEY_0x13
* Volume Label (Root Directory): XOR_KEY_0x13

This provides a vital cryptographic clue: any hidden payload is likely obfuscated using an XOR cipher with the key 0x13 (decimal 19)

### Step 2: File Listing and Inspection

Next, we list the files stored on the image to locate potential hiding spots:

```
fls -f fat usb_dump.raw
```

Output shows a single file: `r/r 5: vacation.txt`.

If we inspect the content of this file, it contains the string `VACATION_PHOTO_METADATA_XOR_PROTECTED_BKP`. This confirms that encrypted data is tied to this specific file context.

### Step 3: Slack Space Extraction

Since the payload is hidden in the "slack space" (the unused area at the end of an allocated sector cluster) and running strings on the raw image yields nothing due to the encryption, we must isolate the slack space blocks.

We use blkls with the -s flag to extract only the slack space of active files into a separate binary: 

```
blkls -f fat -s usb_dump.raw > slack.bin
```

### Step 4: Decryption
Now that the obfuscated bytes are isolated in slack.bin, we apply the XOR key (0x13 / 19) discovered in Step 1. This can be done via a quick Python inline script to decrypt the stream and filter out empty null bytes:

```
python3 -c "print(''.join(chr(b ^ 19) for b in open('slack.bin', 'rb').read() if b != 0))"
```