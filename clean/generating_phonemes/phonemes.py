import json
import math

from g2p_en import G2p

g2p = G2p()

file_name = 'jamal.json' 
with open(file_name, 'r') as f:
  data = json.load(f)


FRAME_PER_SECOUND = 24
AUDO_END_TIME = data['fragments'][-1]['end']
EXTRA_TIME = 5
AUDO_END_TIME = math.ceil(  float(AUDO_END_TIME) + EXTRA_TIME)

print("FRAME_PER_SECOUND:" ,  FRAME_PER_SECOUND)
print( "AUDO_END_TIME  : "  , AUDO_END_TIME)



print(data['fragments'][0])
for each_data in data.get('fragments'):
    each_data['phonemes'] = g2p(each_data['lines'][0])

    each_data['init_frame'] = math.ceil(  float(each_data['begin']) * FRAME_PER_SECOUND )
    each_data['final_frame'] = math.ceil(  float(each_data['end']) * FRAME_PER_SECOUND)

    each_data['diff'] = math.ceil(  (each_data['final_frame'] - each_data['init_frame']) / len(each_data['phonemes']))


data['FRAME_PER_SECOUND'] = FRAME_PER_SECOUND
data['AUDO_END_TIME'] = AUDO_END_TIME
data['TOTAL_VIDEO_FRAMES'] = AUDO_END_TIME * FRAME_PER_SECOUND

with open(file_name.split('.')[0]+"_phonemes.json", "w") as outfile:
    json.dump(data, outfile)