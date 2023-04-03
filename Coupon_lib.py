#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def heating(t0):
    # Preset Heating Function 20 - 850 °C in 
    T_set = [0,0,0,0]
    MFC_set = [3750,0,0]

    T_low = 20
    T_high = 850
    heat_time = 4500
    run_time = 5400
    if (time.time() -t0) < heat_time:
        T_calc = T_low + (T_high-T_low) /(heat_time) * (time.time() -t0)
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]

    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]

    return T_set, MFC_set, t_end

def heating_450(t0):
    # Preset Heating Function 450 - 850 °C in 
    T_set = [0,0,0,0]
    MFC_set = [3750,0,0]

    T_low = 450
    T_high = 850
    heat_time = 2700
    run_time = 3600
    if (time.time() -t0) < heat_time:
        T_calc = T_low + (T_high-T_low) /(heat_time) * (time.time() -t0)
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]

    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]

    return T_set, MFC_set, t_end



def Coking(t0):
    T_set = [0,0,0,0]
    MFC_set = [0,0,833]

    T_low = 850
    T_high = 986
    heat_time = 3600
    run_time = 3600*6
    if (time.time() -t0) < heat_time:
        T_calc = T_low + (T_high-T_low) /(heat_time) * (time.time() -t0)
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]

    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]

    return T_set, MFC_set, t_end

def Cooling(t0):
    T_set = [0,0,0,0]
    MFC_set = [3750,0,0]

    T_low = 986
    T_high = 850
    heat_time = 900
    run_time = 1800
    if (time.time() -t0) < heat_time:
        T_calc = T_low + (T_high-T_low) /(heat_time) * (time.time() -t0)
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]
        
    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]
    return T_set, MFC_set, t_end

def Cooling_450(t0):
    T_set = [0,0,0,0]
    MFC_set = [3750,0,0]

    T_low = 1000
    T_high = 450
    heat_time = 7200
    run_time = heat_time
    if (time.time() -t0) < heat_time:
        T_calc = T_low + (T_high-T_low) /(heat_time) * (time.time() -t0)
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]
        
    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]
    return T_set, MFC_set, t_end
    
def Decoking(t0):
    T_set = [0,0,0,0]
    MFC_set = [1250,1250,0]

    T_low = 850
    T_high = 1000
    run_time = 1800
    T_calc = T_low + (T_high-T_low) /(run_time) * (time.time() -t0)
    T_set = [T_calc,T_calc,T_calc,T_calc]

    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [T_high,T_high,T_high,T_high]
    return T_set, MFC_set, t_end

def SteamTreatment(t0):
    T_set = [1000,1000,1000,1000]
    MFC_set = [0,1250,0]
    run_time = 900
    t_end = run_time - (time.time() -t0)
    if (t_end < 0):
        MFC_set = [3750,0,0]
        T_set = [850,850,850,850]
    return T_set, MFC_set, t_end