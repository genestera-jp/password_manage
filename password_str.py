import string
import secrets

def pass_make(size=8):
  chars = string.ascii_letters + string.digits
  return ''.join(secrets.choice(chars) for i in range(size))

print(pass_make())
