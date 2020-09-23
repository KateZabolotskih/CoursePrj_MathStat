import matplotlib.pyplot as plt
import xlrd
import os

xlsx_files_path = "xlxs/"

NUM_OF_DISCHARGES = 5
DISCHARGE = 38215
DISCHARGES = [38215, 38216, 38217, 38218, 38219, 38220, 38221, 38222, 38252, 38253]

# Function that saves files with the specified names and format
# The default format is "png"
def save(name='', format='png'):
    pwd = os.getcwd()
    iPath = 'pictures/{}'.format(format)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, format))
    os.chdir(pwd)

# Function for displaying a graph of temperature versus time
# The save function in png format is also called here
def draw_data(x, y, title):
    plt.figure()
    plt.plot(x, y, label='line', color='tomato', linewidth=0.5)
    plt.title(title)
    plt.xlabel('time')
    plt.ylabel('temperature')
    plt.grid(True)
    save(title, 'png')
    #plt.show()

# Function gets data for the first n(number of discharges) in the worksheet
# It also calls a function to draw data
def getData_byNum(num_of_dis, worksheet):
    cur_discharge = worksheet.cell(1, 1).value
    prev_discharge = cur_discharge
    row = 1  # start position in table
    col = 2  # start position in table

    for i in range(num_of_dis):
        data = []
        while cur_discharge == prev_discharge:
            time = (worksheet.cell(row, col).value)
            temperature =(worksheet.cell(row, col + 1).value)
            data.append({'time': time, 'temperature': temperature})
            row += 1
            cur_discharge = worksheet.cell(row, 1).value
        time = []
        temperature = []
        for el in data:
            time.append(el['time'])
            temperature.append(el['temperature'])
        draw_data(time, temperature, str(prev_discharge) + "_discharge_res_XLSX")
        prev_discharge = cur_discharge

# The function finds data by the specified discharge
# It also calls a function to draw data
def getData_byDis(discharge, worksheet):
    cur_discharge = worksheet.cell(1, 1).value
    row = 1  # start position in table
    col = 2  # start position in table
    # trying to find the right discharge
    while cur_discharge != discharge:
        row += 1
        cur_discharge = worksheet.cell(row, 1).value

    data = []
    # reading data for this discharge
    while cur_discharge == discharge:
        time = (worksheet.cell(row, col).value)
        temperature = (worksheet.cell(row, col + 1).value)
        data.append({'time': time, 'temperature': temperature})
        row += 1
        cur_discharge = worksheet.cell(row, 1).value

    time = []
    temperature = []
    for el in data:
        time.append(el['time'])
        temperature.append(el['temperature'])
    draw_data(time, temperature, str(discharge) + "_discharge_res_XLSX")

def read_xlsx_file(file_name):
    # open the file
    workbook = xlrd.open_workbook(file_name)
    # selecting a page to read by index
    worksheet = workbook.sheet_by_index(0)
    getData_byNum(NUM_OF_DISCHARGES, worksheet)
    getData_byDis(DISCHARGE, worksheet)

    # You can go through the list of discharges
    #for dis in DISCHARGES:
    #   getData_byDis(dis)


if __name__ == '__main__':
    read_xlsx_file(xlsx_files_path + "TS_results" + ".xlsx")
