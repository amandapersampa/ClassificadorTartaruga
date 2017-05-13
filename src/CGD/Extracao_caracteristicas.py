from setuptools.command.rotate import rotate
from skimage.feature import local_binary_pattern
from scipy.misc import imread
from time import time
import numpy as np

#def minimum_value(original):
#    aux = original
#    rotationed = rotate(original)
#    max = 9
#    i = 0
#    while (i < max):
#        if (rotationed < aux):
#            aux = rotationed
#        rotationed = rotate(rotationed)
#        i = i + 1
#    return aux

#def rotate(value):
#    if (value % 2 == 0):
#        return value >> 1
#   else:
#        value = value >> 1
#    return value + 256

def localBinary(img, lbp='default'):
    radius = 3
    n_points = 8 * radius
    lbp = local_binary_pattern(img, n_points, radius, lbp).astype(np.int64)
    #for i in range(len(lbp)):
    #    for j in range(len(lbp)):
    #        lbp[i][j] = minimum_value(lbp[i][j])
    return lbp

def histograma(channel):
    histogram, bin_edges = np.histogram(channel)
    hist = histogram
    hist = hist.tolist()
    return hist

def  characteristic_matrix_lbp_RGB (nome, lbp='default') :
    return characteristic_matrix_lbp(nome, 'RGB', lbp=lbp)

def  characteristic_matrix_lbp_YCbCr(nome,lbp='default') :
    return characteristic_matrix_lbp(nome, 'YCbCr', lbp=lbp)

def characteristic_matrix_lbp(nome, tipo, lbp):
    tart = imread(nome, mode=tipo)
    channel_0 = localBinary(tart[:, :, 0], lbp=lbp)
    hist = histograma(channel_0)
    channel_1 = localBinary(tart[:, :, 1], lbp=lbp)
    hist.extend(histograma(channel_1))
    channel_2 = localBinary(tart[:, :, 2], lbp=lbp)
    hist.extend(histograma(channel_2))
    return hist

