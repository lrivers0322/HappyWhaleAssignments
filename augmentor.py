# load in the dataset from the csv file
import csv
import cv2 as cv
import keras_preprocessing.image.utils
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os.path
from keras.preprocessing.image import ImageDataGenerator

# This does not rely on RAM I don't think because the images are never in a singular array. I take them,
# put them into an array, save them, and then overwrite them with the next image.

# THIS IS THE AMOUNT OF IMAGES THAT THE THING WILL GENERATE
numImages = 10000
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# Opens the csv file with the paths and labels of the animals although I guess I don't need this
csvfile = open('C://Users//ltriv//Downloads//Happy-whale-and-dolphin//train.csv', mode='r')
csvfile = csv.reader(csvfile)
directory = 'C://Users//ltriv//Downloads//Happy-whale-and-dolphin//train_images'
species = []
paths = []
images = []

# appends each coloum to the proper list.
for i in csvfile:
    species.append(i[1])
    paths.append(i[0])
# has to remove the label at the top of each coloum.
paths.remove('image')
specieslist = []

i = 0
m = 0
# collects a list of all the species
while i < 29:
    if not species[m] in specieslist:
        specieslist.append(species[m])
        i += 1
    m += 1
# removes the headers
specieslist.remove('species')
species.remove('species')
q = 0
# sets the species names to their index in the specieslist list
for n in species:
    appender = specieslist.index(n)

    species[q] = np.array([appender])
    q += 1
species = np.asarray(species)
species = species.astype('uint8')
print(os.path.join(directory, paths[0]))

pathes = []
for i in paths:
    pathes.append(directory + "//" + i)
print(pathes)

imagees = np.zeros(shape=(1, 32, 32, 3))
i = 0

# Image data generator. change the values inside or add you new ones.
imageGen = ImageDataGenerator(width_shift_range=.3, height_shift_range=.3, horizontal_flip=True, zoom_range=.3)
# Change the number in each of these next two for loops to adjust how many images it adds. This could be consolidated
# into one for loop but I was lazy
for l in range(numImages):
    # adjust the tuple inside of cv.resize to adjust resolution
    temp = cv.resize(cv.imread(os.path.join(directory, pathes[l])), (32, 32))
    imagees[0] = (cv.cvtColor(temp, cv.COLOR_BGR2RGB))

    print(imagees.shape)

    it = imageGen.flow(imagees)
    im = it.next()
    im = im[0].astype('float32')

    im = im / 255.0
    # this line takes the path, removes .jpg, adds "trial", and then adds jpg again and then saves a PIL IMage to the
    # folder below.

    keras_preprocessing.image.utils.array_to_img(im).save(
        "C://Users//ltriv//Downloads//testingimages//" + paths[l][:len(paths[l]) - 4] + "trial.jpg")
