# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:54:24 2022

@author: shanto
"""

import Labber
import os
import sys
from utilities import Watt2dBm, dBm2Watt, VNA2dBm

from jpa_tune_up_helper_functions import *

if __name__ == "__main__":
    labber_data_file = str(input("Labber File Location: "))
    repeated = int(input("Number of Repeations: "))
    power_range = int(input("Number of Points for Power: "))
    freq_range = int(input("Number of Points for Source Current: "))

    std_highSNR = 1.15 # cut off point for determining high SNR
    cutOff_around_SA_peak = 10e3 # Hz

    lf = Labber.LogFile(labber_data_file)

    power_channel_name = "1000334C - Power"
    freq_channel_name = "1000334C - Frequency"
    current_channel_name = "Victor - Source current"
    SA_channel_name = 'HP Spectrum Analyzer - Signal'

    pump_power = lf.getData(name = power_channel_name)
    jpa_current = lf.getData(name = current_channel_name)

    signal = lf.getData(name = SA_channel_name)
    linsig = dBm2Watt(signal)

    SAxdata, SAydata = lf.getTraceXY(y_channel=SA_channel_name) # gives last trace from SA

    plt.rcParams['savefig.facecolor']='white'

    get_SNR_space_plot(signal,repeated, freq_range, power_range, jpa_current,
                       pump_power, SAxdata, cutOff=cutOff_around_SA_peak,
                       title="JPA Tune Up", xlabel='Pump Power (dBm)', 
                       ylabel='Source Current (mA)', zlabel='SNR', 
                       fig_type=".png", path="figures")

