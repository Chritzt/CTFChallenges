import marshal
import dis

with open("challenge.pyc", "rb") as f:
    header = f.read(16)
    code_obj = marshal.load(f)

print("--- DISASSEMBLIERTER BYTECODE ---")
dis.dis(code_obj)