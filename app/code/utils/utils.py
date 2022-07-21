def path_creation_for_mouth(character_number=1, mouth_type="happy"):
    path = f"./images/mouth/character_{character_number}/{mouth_type}/"
    return path
    

def path_creation_for_eyes(character_number=1, eyes_type="", eyes_emotion="happy",intensity=False, eyes_position="L"):
    """1.  character_number: which character to use (1-6)
    2.  eyes_type: which eyes to use (blinking or not) 
    3.  eyes_emotion: which emotion to use (happy, angry, sad, surprised, confused, sleepy) 
    4.  intensity: if True, use intensity images, if False, use normal images
    5.  eyes_position: which eyes to use (L or R or M) """

    path = f"./images/eyes/character_{character_number}/side_eyes"

    if eyes_type == "blinking":
        eyes_type = f"_{eyes_type}"
        path += eyes_type+"/"
    else:
        path += "/"
    path += f"{eyes_emotion}"

    if intensity:
        path += "_2/"
        #image name
        path += f"{eyes_emotion}_2_{eyes_position}.png"
    else:
        path += "/"
        path += f"{eyes_emotion}_{eyes_position}.png"


    return path