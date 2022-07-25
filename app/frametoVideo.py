
import cv2
import numpy as np
import os
import json

from os.path import isfile, join
mypath = './frames/headFrames/'

frame_data = open('./json/json_data_for_frame/jamal_phonemes.json')

frame_data = json.load(frame_data)


def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))
    

    for counter in range(frame_data['TOTAL_VIDEO_FRAMES']):

                # print(number)
            files = str(counter) + '.png'
            print(files)

            filename=pathIn + files
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            print(filename)
            #inserting the frames into an image array
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= './frames/headFrames/'
    pathOut = 'video2.avi'
    fps = 24.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()