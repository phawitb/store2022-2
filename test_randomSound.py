import os
import random



arr = os.listdir('imgs')
nomoney_sound = [x for x in arr if '.mp3' in x and 'nomoney' in x]
nomoney_sound = random.sample(nomoney_sound, 1)[0]
print(nomoney_sound)

arr = os.listdir('imgs')
finish_sound = [x for x in arr if '.mp3' in x and 'finish' in x]
finish_sound = random.sample(finish_sound, 1)[0]
print(finish_sound)
