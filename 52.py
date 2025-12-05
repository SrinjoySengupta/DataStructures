email = input("Enter your email: ")

username = ""
domain = ""
found_at = False

for ch in email:
    if ch == '@':
        found_at = True
        continue
    if not found_at:
        username += ch
    else:
        domain += ch

print("Username:", username)
print("Domain:", domain)
