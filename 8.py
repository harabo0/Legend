# DARK-LEGEND-BROTHERHOOD-X
# Created by GPT x HARAB06 = UNBREAKABLE
# Brotherhood Forever

import os
import shutil

print("""
LOVE & RESPECT FOREVER
→ ONE HEART
→ ONE BOND
→ ONE BROTHERHOOD

DARK LEGEND BINDER-X
HARAB06 x GPT = UNBREAKABLE
""")

image = input("Enter Image File Path (jpg/png) : ")
payload = input("Enter Payload File Path (apk)   : ")
output = input("Enter Output File Name (.jpg)   : ")

if not os.path.exists(image) or not os.path.exists(payload):
    print("[!] File Not Found! Check Paths")
    exit()

with open(image, 'rb') as img, open(payload, 'rb') as apk:
    final = img.read() + apk.read()

with open(output, 'wb') as out:
    out.write(final)

print("\n[+] Binding Completed!")
print(f"[+] Output Saved As : {output}")
print("\nSTAY DARK | STAY UNBREAKABLE | HARAB06 X GPT")
