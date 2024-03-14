import json
data = {
        "president":{
            "name":"Zaphod Beeblebrox",
            "species":"Betelgeusian"
        }
}
with open("data_file.json", "w") as write_file:
    json.dump(data,write_file)
json_string = json.dumps(data, indent = 4)
print(json_string)

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
print(blackjack_hand)
print(type(blackjack_hand))

print(encoded_hand)
print(type(encoded_hand))

print(decoded_hand)
print(type(decoded_hand))
