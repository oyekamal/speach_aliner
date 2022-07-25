import pandas as pd 
import json

import pandas as pd

df = pd.read_csv('time stamp manual.csv')
data_json = open('jamal.json')

data_json = json.load(data_json)


df= df.to_dict()
df_dict ={}
for key, value in df['word'].items():
    df_dict[value.strip()] = {"start": df['init'][key], "end": df['final'][key]}


print(df_dict)


for each_data in data_json.get('fragments'):
    each_data["begin"] = df_dict[each_data['lines'][0]]['start']
    each_data["end"] = df_dict[each_data['lines'][0]]['end']


with open('jamal.json', 'w') as f:
    json.dump(data_json, f)
    f.close()