x = "848f3d0-804b000-80489c3-f7fb7d80-ffffffff-1-848d160-f7fc5110-f7fb7dc7-0-848e180-3-848f3b0-848f3d0-6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-34636462-61653532-ffbb007d-f7ff2af8-f7fc5440-23e6df00-1-0-f7e54ce9-f7fc60c0-f7fb75c0-f7fb7000-ffbb61c8-f7e4568d-f7fb75c0-8048eca-ffbb61d4-0-f7fd9f09-804b000-f7fb7000-f7fb7e20-ffbb6208-f7fdfd50-f7fb8890-23e6df00-f7fb7000-804b000-ffbb6208-8048c86"
s = ""
for i in x.split('-'):
    if len(i) == 8:
        for b in reversed(bytearray.fromhex(i)):
            s += chr(b)

print(s)    
