import matplotlib.pyplot as plt
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
pyglobus_dir = os.path.join(current_dir, "pyglobus", "python")
sys.path.append(pyglobus_dir)
try:
    import pyglobus
except ImportError as e:
    print("Cannot import pyglobus from %s, exiting" % pyglobus_dir)
    sys.exit(1)

sht_files_path = "sht/"
SigROI = [18, 19, 20, 26, 55]
SHT_NUMBER_ARRAY = [38215]

# Function that saves files with the specified names and format
# The default format is "png"
def save(name='', format = 'png'):
    pwd = os.getcwd()
    iPath = 'pictures/{}'.format(format)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, format))
    os.chdir(pwd)

def plot_signals(SHT_NUMBER, SigROI):
    for i in SigROI:
        fig, ax = plt.subplots()

        sht_reader = pyglobus.util.ShtReader(PATH_TO_SHT_FILE)
        signal = sht_reader.get_signal(i)
        x, y = signal.get_data_x(), signal.get_data_y()

        ax.plot(x, y, linewidth=0.5, color='b', label='1')
        title_str = 'ShotNo= ' + str(SHT_NUMBER) + ' Signal= ' + str(i)
        # print(title_str)
        plt.title(title_str)
        save(title_str, 'png')


if __name__ == '__main__':
    plt.rc('figure', max_open_warning = 0)
    for sht in SHT_NUMBER_ARRAY:
        PATH_TO_SHT_FILE = sht_files_path + "sht" + str(sht) + ".SHT"
        #print(PATH_TO_SHT_FILE)
        plot_signals(sht, SigROI)
        # clear memory
        plt.clf()
