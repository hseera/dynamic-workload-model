# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''Default parameter values for the dynamic workload.
Update them to generate the right workload model.
'''
DURATION = 3600
Y1_AMPLITUDE = 25
Y2_AMPLITUDE = 25
Y1_NO_OF_CYCLES = 12
Y2_NO_OF_CYCLES = 4
Y1_HORIZONTAL_SHIFT = 0
Y2_HORIZONTAL_SHIFT = 0
Y1_VERTICAL_SHIFT = 25
Y2_VERTICAL_SHIFT = 25

'''Default values for a sustain load model.
Update them to with the correct rampu and rampdown duration
'''
RAMPUP = 400
RAMPDOWN = 400
TIME=np.linspace(0,DURATION,DURATION)


#step function
def linear_step_func(x,x0,x1):
    y= np.piecewise(x, [
        x < x0, 
       (x >= x0) & (x <= x1), 
        x > x1],
            [0.,
            lambda x: x/(x1-x0)+x0/(x0-x1), 1.])
    return y

#Using two cosine wave functions to generate a dynamic workload model
def workload_function(T, y1Amplitude, y2Amplitude, y1NoofCycles, y2NoofCycles, y1HozShift, y2HozShift, y1VerShift, y2VerShift):
    workloadModel = []
    x = np.arange(0,T)
    y1= -y1Amplitude*np.cos(y1NoofCycles*np.pi*x/T - y1HozShift) + y1VerShift
    y2= -y2Amplitude*np.cos(y2NoofCycles*np.pi*x/T - y2HozShift) + y2VerShift
    workloadModel.append((x, y1+y2))
    return workloadModel


#function to generate data for the sustain workload model
def sustain_function(rampup,rampdown,duration, time):
    workloadModel = []
    workloadModel.append((time,(linear_step_func(time,0,rampup)+linear_step_func(time,duration-rampdown,duration)*-1)*100))
    return workloadModel

def main():
    
    #Generate a dynamic workload model
    model = workload_function(DURATION,Y1_AMPLITUDE,Y2_AMPLITUDE,Y1_NO_OF_CYCLES,
                Y2_NO_OF_CYCLES,Y1_HORIZONTAL_SHIFT,Y2_HORIZONTAL_SHIFT,Y1_VERTICAL_SHIFT,Y2_VERTICAL_SHIFT)
    
    #Generate a sustain workload model with rampup and rampdown
    #model = sustain_function(RAMPUP,RAMPDOWN,DURATION,TIME)
    
    '''Using below to plot a graph to show what kind of workload model the above code generates with default function values. 
    '''
    x_val = [x[0] for x in model]
    y_val = [x[1] for x in model]
    
    # plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'-_r')
    plt.show()

if __name__ == "__main__":
    main()
    
