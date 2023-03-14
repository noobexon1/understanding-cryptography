import substitution_cipher

# TODO: create decrypt() and implement the cracking technics

plaintext = "Ligma Ball Z Motherfucker XD"
substitution_table = substitution_cipher.create_substitution_table()

cipher = substitution_cipher.encrypt(plaintext, substitution_table)

print(substitution_table)
print(cipher)
