from sys import exec_prefix
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == "__main__":
    f = open("edgecloud-simulator-daohiep/4_20_80_1020_10150_120/VNFGApp/cent_1_event.csv")
    data = csv.reader(f)

    power = [0]*11
    count = [0]*11

    for row in data:
        if row[9] != '-' and row[9] != 'util':
            i = round(float(row[9])/10)
            power[i] = (power[i]*count[i] + float(row[11]))/(count[i]+1)
            count[i] += 1
    
    while True:
        try:
            power.remove(0)
        except:
            break

    plt.plot([i*10 for i in range(len(power))], power, c="r")
    plt.xlabel("Utilization (%)")
    plt.ylabel("Power Consumption (W)")

    plt.show()
    
    f.close()
