import math, csv, datetime
import numpy as np

import matplotlib.pyplot as plt

from skimage.io import imshow, imread, imsave

with open("earthquakes.csv", "r") as file:
    reader = csv.reader(file)
    data = np.array(list(reader))



def dateHisto():
    #dates = data[].
    
    plt.figure("dateHisto", figsize=[7,7])
    #plt.xlim([-180,180])
    #plt.ylim([-90,90])

    plt.scatter()

    plt.show()





def magMap():
    longlat = [data[1:,8].astype(float), data[1:,6].astype(float)]
    mag = data[1:,9].astype(float)




    plt.figure("magMap", figsize=[14,8])
    plt.xlim([-180,180])
    plt.ylim([-90,90])

    bakmap = plt.imread("map/map.jpg")
    plt.imshow(bakmap, extent=[-180,180,-90,90])

    plt.scatter(longlat[0], longlat[1], c=mag, cmap="viridis")
    plt.colorbar()

    plt.show()



#dateHisto()


