from hash_password import HashPassword


hash_password = HashPassword()

plain_password = "my-password"

hashed_password = hash_password.create_hash(plain_password)
print(hashed_password)

match = hash_password.verify_hash(plain_password, hashed_password)
print(match)

hashed_password = hash_password.create_hash_with_salt(plain_password, "a" * 21 + "e")
print(hashed_password)

match = hash_password.verify_hash(plain_password, hashed_password)
print(match)
