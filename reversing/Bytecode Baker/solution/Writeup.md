## Bytecode Baker 

Welcome to Initech's secure licensing portal! We locked our newest software version behind a compiled Python script. Can you bypass the validation and retrieve the flag?

Provided files: challenge.pyc

### Reconnaissance

Running the standard Linux strings utility on the provided .pyc file reveals no plain-text flags or hardcoded secrets. A quick check of the bytecode using Python's built-in dis module shows that the program expects a 16-character license key and validates it using a mathematical formula based on the character positions and their ASCII values.

### Solution

We have two primary ways to solve this challenge: Mathematical Reversing or Bytecode Patching.

#### Approach 1: Reversing the Mathematics (The Intended Way)

Looking at the disassembly the validation loop checks the following condition for each character at index i: 

$$\text{ord}(\text{key}[i]) \times (i + 1) = \text{target}[i]$$

The target array extracted from the bytecode constants is: `[720, 484, 528, 444, 435, 786, 686, 736, 810, 800, 847, 984, 756, 858, 870, 1040]` 

We can write a simple Python script to reverse this operation and calculate the correct license key:

```Python
targets = [720, 484, 528, 444, 435, 786, 686, 736, 810, 800, 847, 984, 756, 858, 870, 1040]
key = "".join([chr(target // (i + 1)) for i, target in enumerate(targets)])
print("Valid Key:", key)

```

Running this script gives us the valid license key. Supplying it to the program successfully passes the check, decrypts the internal XOR-encrypted payload (using key 0x5A), and reveals the flag.