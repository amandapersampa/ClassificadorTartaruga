import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(target, cm, title='Confusion matrix', cmap=plt.cm.Blues, lbp='default'):
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    width = len(cm)
    for x in range(width):
        for y in range(width):
            ax.annotate(str(cm[x][y]), xy=(y, x),
                        horizontalalignment='center',
                        verticalalignment='center')
    plt.title(title)
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Reds)
    plt.colorbar(fraction=0.046, pad=0.04)
    tick_marks = np.arange(len(target))
    plt.xticks(tick_marks, target, rotation=45)
    plt.yticks(tick_marks, target)
    plt.ylabel(u'Classe Verdadeira', fontsize=16)
    plt.xlabel(u'Classe Estimada', fontsize=16)

    plt.tight_layout()

    title = lbp+'-'+title +'.png'
    plt.savefig(title)
    plt.close(fig)


def saveImages_erro(error_file, name_test, name_pred, clf_name, mode_name):
    iterate = 0
    for i in range(len(error_file)):
        fig = plt.figure()
        plt.imshow(error_file[i])
        folder = 'pred-' + name_pred[i] + '-esp-' + name_test[i]
        base = '.\\CGT\\Result\\' + clf_name + '\\' + mode_name + '\\' + folder
        plt.title('Especie: ' + name_test[i] + ' - Previsto: ' + name_pred[i])
        file = 'Imagem-original'
        title = base + '\\' + str(i) + file + '.png'
        plt.savefig(title)
        plt.close(fig)
        print("File: " + title + " Salvo")
        iterate+=1
'''
def saveImagemClassificador():
    n_neighbors = 15

    # import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # we only take the first two features. We could
    # avoid this ugly slicing by using a two-dim dataset
    y = iris.target

    h = .02  # step size in the mesh

    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
                  % (n_neighbors, weights))

    plt.show()
'''