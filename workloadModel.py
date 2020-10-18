# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:46:53 2020

@author: harinder
"""


import numpy as np
import matplotlib.pyplot as plt


#using two cosine wave functions to generate a workload model
def workload_function(T, y1Amplitude, y2Amplitude, y1NoofCycles, y2NoofCycles, y1HozShift, y2HozShift, y1VerShift, y2VerShift):
    workloadModel = []
    x = np.arange(0,T)
    y1= -y1Amplitude*np.cos(y1NoofCycles*np.pi*x/T - y1HozShift) + y1VerShift
    y2= -y2Amplitude*np.cos(y2NoofCycles*np.pi*x/T - y2HozShift) + y2VerShift
    t = y1+y2
    workloadModel.append((x,t))
    return workloadModel

def main():
    duration = "" #3600
    y1Amplitude = "" #25
    y2Amplitude = "" #25
    y1NoofCycles = "" #12
    y2NoofCycles = "" #4
    y1HorizontalShift = "" #0
    y2HorizontalShift = "" #0
    y1VerticalShift = "" #25
    y2VerticalShift = "" #25
    
    model = workload_function(duration,y1Amplitude,y2Amplitude,y1NoofCycles,y2NoofCycles,y1HorizontalShift,y2HorizontalShift,y1VerticalShift,y2VerticalShift)
    
    x_val = [x[0] for x in model]
    y_val = [x[1] for x in model]
    
    plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'-_r')
    plt.show()
if __name__ == "__main__":
    main()
    
