import matplotlib.pyplot as plt
import os

DISCHARGE = 38215
txt_res_path = "res_txt/Temperature_SHT"

def save(name='', format='png'):
    pwd = os.getcwd()
    iPath = 'pictures/{}'.format(format)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, format))
    os.chdir(pwd)

def plot(x, y, label_x, label_y, label):
    plt.plot(x[:400], y[:400], label=label, linewidth=2)
    plt.xlabel(label_x)
    plt.ylabel(label_y)

def read_res_txt(file_path):
    NUM_SXR = [80, 50, 15]
    plt.figure(figsize=(20,20))

    for i in range(len(NUM_SXR) - 1):
        for j in range(i + 1, len(NUM_SXR)):
            file_name = file_path + str(DISCHARGE) + "_" + str(NUM_SXR[i]) + "-" + str(NUM_SXR[j]) + ".txt"
            f = open(file_name, 'r')
            X = []
            Y = []
            for num, line in enumerate(f.readlines()):
                if num % 15000 != 0:
                    continue
                x, y = line.split()
                X.append(x)
                Y.append(y)
            plot(X, Y, "Time (ms)", "T (eV)", "R" + str(NUM_SXR[i]) + "-" + str(NUM_SXR[j]))

    plt.title("SHT" + str(DISCHARGE))
    plt.legend()
    save("R" + str(DISCHARGE), 'png')

if __name__ == '__main__':
    read_res_txt(txt_res_path)