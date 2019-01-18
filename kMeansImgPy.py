# I've left some code in comments so that it can be easier if one wants to test and see output at various points. To make things simpler just remove the commented code !

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import utils
import cv2
import numpy as np
import pandas as pd

def kMeansImage(img):
    image = img
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    nC = 3              # No. of Clusters

    # ========= (Can be used to test later)! ======================================
    # show image
    # You can comment the graph if you want only RGB values
    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    # reshape the image to a list of pixels
    # matrix to array
    image = image.reshape((image.shape[0]*image.shape[1],3))

    # cluster the pixel intensities
    # clt = KMeans(n_clusters=args["clusters"])
    clt = KMeans(n_clusters=nC)

    # A call to fit() method clusters our list of pixels
    clt.fit(image)
    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    bar = utils.plot_colors(hist, clt.cluster_centers_)

    colors = clt.cluster_centers_
    labelsIndex = pd.Series(clt.labels_).value_counts().to_frame()
    # .index.tolist()
    print("Cluster count : ")
    print(colors)     # Contains colors

    print("Label count : ")
    print(labelsIndex)  # Contains index of colors (No. of pixels in each clusters)
    
    print("Max cluster count :")
    print(labelsIndex[0].tolist())

    print("Max index :")
    maxIndex = labelsIndex.index.values     # Max color + index Dataframe sorted
    print(maxIndex[0])
    maxColorIndex = maxIndex[0]             # Get max color index
    
    print("Max Color : ")
    print(colors[maxColorIndex])            # Max color

    # Numpy array to list of colors
    colorsList = colors[maxColorIndex].tolist()

    # print("Red Component : "+str(colorsList[0]))
    # print("Green Component : "+str(colorsList[1]))
    # print("Blue Component : "+str(colorsList[2]))

    # ========= For reference ! ======================================

    #Coordinates of cluster centers with shape [n_clusters, n_features]
    # clt.cluster_centers_
    #Labels of each point
    # clt.labels_

    # ========= (Can be used to test later)! ======================================
    # ========= For reference ! ======================================
    # show our color bart
    # You can comment the graph if you want only RGB values
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

    return colorsList
