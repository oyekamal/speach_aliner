import json
import math

from g2p_en import G2p

g2p = G2p()

file_name = 'jamal.json' 
with open(file_name, 'r') as f:
  data = json.load(f)


FRAME_PER_SECOUND = 24
AUDO_END_TIME = data['fragments'][-1]['end']
EXTRA_TIME = 7
AUDO_END_TIME = math.ceil(  float(AUDO_END_TIME) + EXTRA_TIME)

print("FRAME_PER_SECOUND:" ,  FRAME_PER_SECOUND)
print( "AUDO_END_TIME  : "  , AUDO_END_TIME)



print(data['fragments'][0])
for each_data in data.get('fragments'):
    each_data['phonemes'] = g2p(each_data['lines'][0])

    each_data['init_frame'] = math.ceil(  float(each_data['begin']) * FRAME_PER_SECOUND )
    each_data['final_frame'] = math.ceil(  float(each_data['end']) * FRAME_PER_SECOUND)

    each_data['diff'] = math.ceil(  (each_data['final_frame'] - each_data['init_frame']) / len(each_data['phonemes']))

    
    number_of_phonemes = len(each_data['phonemes'])
    if number_of_phonemes < each_data['diff']:
      phonemes_frame = {}
      num, div = each_data['diff'], number_of_phonemes
      count_frame = [num // div + (1 if x < num % div else 0)  for x in range (div)]

      for i in range(len(count_frame)):
        phonemes_frame[each_data['phonemes'][i]] = count_frame[i]
      # equal_diff = each_data['diff'] // number_of_phonemes
      # equal_diff_chck = equal_diff * number_of_phonemes

      # phonemes_frame = {each_phoneme:equal_diff for each_phoneme in each_data['phonemes']}

      # if equal_diff_chck != each_data['diff']:
      #   less_frame = each_data['diff'] - int(equal_diff_chck)
      #   phonemes_frame[list(phonemes_frame.keys())[-1]] = less_frame

    else:
      phonemes_frame = {}
      limited_frame = each_data['diff']
      for each_phoneme in each_data['phonemes']:
        if limited_frame > 0:
          phonemes_frame[each_phoneme] = 1
          limited_frame -= 1
        else:
          phonemes_frame[each_phoneme] = 0
    each_data["phonemes_frame"] = phonemes_frame


data['FRAME_PER_SECOUND'] = FRAME_PER_SECOUND
data['AUDO_END_TIME'] = AUDO_END_TIME
data['TOTAL_VIDEO_FRAMES'] = AUDO_END_TIME * FRAME_PER_SECOUND

with open(file_name.split('.')[0]+"_phonemes.json", "w") as outfile:
    json.dump(data, outfile)