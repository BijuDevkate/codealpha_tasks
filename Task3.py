import re
import os

if not os.path.exists("input.txt"):
    print("input.txt not found")
    exit()

file = open("input.txt", "r", encoding="utf-8")
data = file.read()
file.close()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

out = open("emails.txt", "w", encoding="utf-8")

for e in emails:
    out.write(e + "\n")

out.close()

if len(emails) == 0:
    print("No emails found")
else:
    print(len(emails), "emails extracted and saved to emails.txt")
