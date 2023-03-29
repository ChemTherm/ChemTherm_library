#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def heating(t0):
    # Preset Heating Function 20 - 850 °C in 
    T_set = [0,0,0,0]
    MFC_set = [0,0,0]

    T_high = 850
    T_low = 20
    run_time = 7200
    T_calc = T_low + (T_high-T_low) *(run_time) * time.time() -t0
    T_set = [T_calc,T_calc,T_calc,T_calc]
    MFC_set[0] = 3750
    MFC_set[1] = 0
    MFC_set[2] = 0
    t_end = run_time - (time.time() -t0)
    return T_set, MFC_set, t_end

def Coking(t0):
    T_set = [0,0,0,0]
    MFC_set = [0,0,0]

    T_high = 986
    T_low = 850
    heat_time = 3600
    run_time = 3600*6
    if time.time() -t0 < heat_time:
        T_calc = T_low + (T_high-T_low) *(heat_time) * time.time() -t0
        T_set = [T_calc,T_calc,T_calc,T_calc]
    else:
        T_set = [T_high,T_high,T_high,T_high]

    MFC_set[0] = 0
    MFC_set[1] = 0
    MFC_set[2] = 833
    t_end = run_time - (time.time() -t0)
    return T_set, MFC_set, t_end

def Cooling(t0):
    T_set = [0,0,0,0]
    MFC_set = [0,0,0]

    T_high = 850
    T_low = 986
    run_time = 1800
    T_calc = T_low + (T_high-T_low) *(run_time) * time.time() -t0
    T_set = [T_calc,T_calc,T_calc,T_calc]

    MFC_set[0] = 3750
    MFC_set[1] = 0
    MFC_set[2] = 0
    t_end = run_time - (time.time() -t0)
    return T_set, MFC_set, t_end
    
def Decoking(t0):
    T_set = [0,0,0,0]
    MFC_set = [1250,1250,0]

    T_high = 850
    T_low = 1000
    run_time = 1800
    T_calc = T_low + (T_high-T_low) *(run_time) * time.time() -t0
    T_set = [T_calc,T_calc,T_calc,T_calc]

    t_end = run_time - (time.time() -t0)
    return T_set, MFC_set, t_end

def SteamTreatment(t0):
    T_set = [1000,1000,1000,1000]
    MFC_set = [0,1250,0]
    run_time = 900
    t_end = run_time - (time.time() -t0)
    return T_set, MFC_set, t_end