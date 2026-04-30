import pyotp
secret =pyotp.random_hex()
print(f"segreto generato: {secret} {len(secret)}")