import hashlib


sha256_hash = hashlib.sha256()

sha256_hash.update(input().encode("utf-8"))

print(sha256_hash.hexdigest())
