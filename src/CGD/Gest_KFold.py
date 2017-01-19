import pickle

base = '.\\CGD\\base\\'


def saveKfold(kfold):
    output = open(base + 'kFold.pkl', 'wb')
    pickle.dump(kfold, output)
    output.close()


def upload_Kfold():
    filename = base + 'kFold.pkl'
    with open(filename, "rb") as f:
        kfold = pickle.load(f)
    return kfold
