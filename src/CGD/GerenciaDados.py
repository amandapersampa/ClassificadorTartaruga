import os
import pickle
from scipy.misc import imread

from src.CDP.Turtle import Turtle
from src.CGD.Extracao_caracteristicas import characteristic_matrix_lbp_RGB
from src.CGD.Extracao_caracteristicas import characteristic_matrix_lbp_YCbCr
from time import time
base = '.\\CGD\\base\\'
source = ['carettacaretta','cheloniamydas','dermochelyscoriacea','eretmochelysimbricata','lepidochelysolivacea']

def base_update(lbp='default'):
    output = open(base+'data.pkl', 'wb')
    i = 1
    for turtle in source:
        path = base
        dir = os.listdir(path+turtle)
        for file in dir:
            nome = path+ turtle + "\\" + file
            tart = imread(nome)
            t = Turtle(turtle,tart)
            t0 = time()
            t.rgb = characteristic_matrix_lbp_RGB(path+ turtle + "\\" + file,lbp=lbp)
            t.ycbcr = characteristic_matrix_lbp_YCbCr(path +turtle + "\\" + file, lbp=lbp)
            pickle.dump(t, output)
            print("Saved in file %d: done in %0.3fs" % (i,(time() - t0)))
            i =i +1
    output.close()

def base_recover():
    filename = base+'data.pkl'
    list = []
    i = 0
    with open(filename, "rb") as f:
        while True:
            try:
                t0 = time()
                t = pickle.load(f)
                list.append(t)
                #print("Loaded file %d: done in %0.3fs" % (i, (time() - t0)))
                i +=1
            except EOFError:
                break
    return list

#t0 = time()
#base_update()
#print("Base Update: done in %0.3fs" % (time() - t0))

#t0 = time()
#print(len(base_recover()))
#print("Base Recover: done in %0.3fs" % (time() - t0))