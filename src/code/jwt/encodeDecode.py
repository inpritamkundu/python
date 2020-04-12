import jwt

# Encode
# encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
# print(encoded_jwt)

# Decode
# decoded_jwt = jwt.decode(encoded_jwt, 'secret', algorithms='HS256')
# print(decoded_jwt)


# decoding using values:

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyRGV0YWlscyI6eyJwcml2aWxlZ2VUeXBlIjoiQ1VTVE9NRVIiLCJtaWRkbGVOYW1lIjpudWxsLCJsYXN0TmFtZSI6Imt1bmR1IiwiaXNFbWFpbFZlcmlmaWVkIjp0cnVlLCJpc01vYmlsZVZlcmlmaWVkIjpmYWxzZSwiaXNBY2NvdW50VmVyaWZ5Ijp0cnVlLCJpc0FjY291bnRTdGF0dXMiOnRydWUsImNsaWVudFR5cGUiOiJXRUIiLCJhZGRyZXNzIjpudWxsLCJfaWQiOiI1ZGQ4Y2MzNzNlOTM5ZDNkYjM1NzRmMzMiLCJ1c2VyTmFtZSI6InByaXRhbWt1bmR1NjBAZ21haWwuY29tIiwiZW1haWwiOiJwcml0YW1rdW5kdTYwQGdtYWlsLmNvbSIsIm1vYmlsZSI6IjkzMzc3MDQ0OTUiLCJmaXJzdE5hbWUiOiJwcml0YW0iLCJwYXNzd29yZCI6IiQyYSQxMCRSVUtJbnNlaVhjUnEwTS5Ldk1ZQjV1RDJEQzBrV3YvZDNNNzlYVDIwczRPYjlrTzI5UDlyMiIsImdlbmRlciI6bnVsbCwiZG9iIjpudWxsLCJyZW1hcmsiOiJ1c2VyIHJlZ2lzdGVyZWQgYW5kIHZlcmlmaWVkIn0sImlhdCI6MTU4NjYxNDYwMCwiZXhwIjoxNTg3MjE5NDAwfQ.3PcQ8mfj9r5sEhO34rG2IZmfrvjq3CWQ_cOkH7Md3fU'
# token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U'
# To convert in bytes
t = token.encode('utf-8')
print(t)
print(type(t))
decoded_jwt = jwt.decode(t, 'organizationId', algorithms='HS256')
print(decoded_jwt)
