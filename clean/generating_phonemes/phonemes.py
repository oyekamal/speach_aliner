import json
from g2p_en import G2p
g2p = G2p()

file_name = 'jamal.json' 
with open(file_name, 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)
print(data['fragments'][0])
for each_data in data.get('fragments'):
    each_data['phonemes'] = g2p(each_data['lines'][0]) 


with open(file_name.split('.')[0]+"_phonemes.json", "w") as outfile:
    json.dump(data, outfile)