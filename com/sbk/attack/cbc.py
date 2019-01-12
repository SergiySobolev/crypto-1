from com.sbk.hex.func import str_to_hex, hex_xor

encrypted_message_hex = '20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d'
iv = encrypted_message_hex.split()[0]
encrypted_message = encrypted_message_hex.split()[1]
real_plain_text = "Pay Bob 100$"
forged_plain_text = "Pay Bob 500$"

real_plain_text_hex = str_to_hex(real_plain_text)
forged_plain_text_hex = str_to_hex(forged_plain_text)

forged_iv = hex_xor(iv, real_plain_text_hex, forged_plain_text_hex)

print(forged_iv + ' ' + encrypted_message)

# 20814804c1767293bd9f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d