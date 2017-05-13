from PIL import Image
from src.CGD.Extracao_caracteristicas import localBinary, histograma
from scipy.misc import imsave, toimage, imread
import matplotlib.pyplot as plt
import numpy as np

root = '.\\CGT\\Result\\'

def save_lbp_RGB(files, name_test, name_pred, clf, mode, tipo, lbp='default'):
   sigla = ["R", "G", "B"]
   save_img(files, name_test, name_pred, clf, mode, sigla, tipo, lbp=lbp)

def save_lbp_YCBCR(files, name_test, name_pred, clf, mode, tipo, lbp='default'):
   sigla = ["Y", "Cb","Cr"]
   save_img(files, name_test, name_pred, clf, mode, sigla, tipo, lbp=lbp)

def save_img(files, name_test, name_pred, clf, mode, sigla, tipo, lbp='default'):
    for count in range(len(files)):
        folder = name_test[count]
        base = root +lbp +'\\' + clf + '\\' + mode + '\\' +  folder
        name = base + '\\' + str(count) + '-' + 'pred-' + name_pred[count]
        arq = name+'.png'
#        try:
#            imread(arq)
#        except:
        imsave(name=arq, arr=files[count])
        print('File: ' + arq + ' Salvo')
        img_tex = []
        hists = []
        #def save(image, count, c, base, rodar=True):
        #def save_hist(file, name_test, name_pred, tipo, count, base):
        img = save(files[count][:, :, 0], sigla[0], name, lbp=lbp)
        img_tex.append(img)
        hists.append(save_hist(img, name_test[count], name_pred[count], sigla[0], count, base))
        img = save(files[count][:, :, 1], sigla[1], name, lbp=lbp)
        img_tex.append(img)
        hists.append(save_hist(img, name_test[count], name_pred[count], sigla[1], count, base))
        img = save(files[count][:, :, 2], sigla[2], name, lbp=lbp)
        img_tex.append(img)
        hists.append(save_hist(img, name_test[count], name_pred[count], sigla[2], count, base))
        create_collage(files[count], img_tex, name+'-tex')

def save_hist(file, name_test, name_pred, tipo, count, base):
    hist, bin_edges = np.histogram(file)
    #print(hist)
    plt.hist(hist, bins='auto', histtype='bar', stacked=True)
    plt.title('Histograma - Especie: ' + name_test + ' - Previsto: ' + name_pred + ' Canal: '+ tipo)
    plt.tight_layout()

    name = 'pred-' + name_pred
    plt.savefig(base + '\\' + str(count)+'-' + name + '-hist-'  + tipo + '.png')
    fig = plt.figure()
    plt.close(fig)
    return hist

def save(image, sigla, arq, lbp='default'):
    img = localBinary(image, lbp)
    imsave(arq + '-lbp-tex-'+ sigla+ '.png', img)
    imsave(arq + '-img-'+sigla + '.png', image)
    return img;
    #print('File: '+ base + '\\' + str(count) + c+'-' + file + '.png Salvo')

def create_collage(img, imgs_tex,  name):
    imgs = []
    imgs.append(img[:, :, 0])
    imgs.append(img[:, :, 1])
    imgs.append(img[:, :, 2])
    cols = 2
    rows = len(imgs)
    width = 160
    height = 240
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    new_im = Image.new('RGB', (width, height))
    i = 0
    x = 0
    y = 0
    for row in range(rows):
        #print(i, x, y)
        im = toimage(imgs[i], channel_axis=2)
        tex = toimage(imgs_tex[i], channel_axis=2)
        new_im.paste(im, (x, y))
        new_im.paste(tex, (x+thumbnail_width, y))
        i += 1
        y += thumbnail_height
    new_im.save(name+".png")