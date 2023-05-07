import pyotp

# key = pyotp.random_base32()
# print(key)
chave_ADM = 'SFNTAXADPJUAFQWZBJFIA3FQBJTVKO36'

chave = pyotp.TOTP(chave_ADM)


def gera_chave():
    return chave.now()


print(chave.now())
