import os
import cv2 as cv
import PySimpleGUI as psg

"""STILL NEED TO MAKE GUI
    """

# Grab the first argument
input_folder = 'C:/Users/Rhine/faceswap2/Faceswap_Workspace/src/extracted faces/_hist_000_by_face/Flip these/'
# Grab the second argument
output_folder = 'C:/Users/Rhine/faceswap2/Faceswap_Workspace/src/extracted faces/_hist_000_by_face/Flip these/'

if not os.path.exists(output_folder):  # Check if the output folder exists
    os.makedirs(output_folder)

count = 0
vert_flip = 0
horz_flip = 1
for image in os.listdir(input_folder):  # Loop through the input folder
    img = cv.imread(f'{input_folder}{image}')
    flipper = cv.flip(img, horz_flip)
    cv.imwrite(f'{output_folder}flipped{image}', flipper)
    count = count + 1
    print(f'Flipping image {count}.....')

print('Task Complete')
