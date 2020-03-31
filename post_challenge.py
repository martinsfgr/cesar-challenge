import string
import json
import hashlib
import requests

answer_json = json.load(open('answer.json'))

end_point = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=6f79cbdd3978211426d28849c5760bbb48337f26"

key = answer_json['numero_casas']
encrypted_text = answer_json['cifrado']

def desencrypt(letters):
    desencrypted_list = list()

    for character in range(0, len(encrypted_text)):
        if encrypted_text[character].isalpha():
            alphabet = string.ascii_lowercase
            index_character = alphabet.index(encrypted_text[character])
            for i in range(0, key):
                if index_character - 1 < 0:
                    index_character = alphabet.index(alphabet[-1])
                else:
                    index_character = index_character - 1
            desencrypted_list.append(alphabet[index_character])
        else:
            desencrypted_list.append(encrypted_text[character])

    desencrypted_text = list()

    for letter in desencrypted_list:
        desencrypted_text.append(letter)
    desencrypted_text = ''.join(desencrypted_text)
    print(desencrypted_text)

    return desencrypted_text

desencrypted_text = desencrypt(encrypted_text)
cryptographic_summary = hashlib.sha1((desencrypted_text).encode('utf-8')).hexdigest()

answer_json['decifrado'] = desencrypted_text
answer_json['resumo_criptografico'] = cryptographic_summary

json_data = answer_json

with open('answer.json', 'w') as f:
    json.dump(json_data, f)

answer = {'answer': ('answer', open('answer.json', 'rb'))}

response = requests.post(url=end_point, files=answer)
print(response.status_code)
