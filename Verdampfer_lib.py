#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def json_timing(config, section, t0):
    T_set = [0,0,0]
    MFC_set = [0]
    
    if config['TIMING']['T_interp'][section] == 0:
        T_set[0] = config['TIMING']['T_Soll1'][section]
        T_set[1] = config['TIMING']['T_Soll1'][section]
        T_set[2] = config['TIMING']['T_Soll2'][section]
    
    else:
        T_set[0] = config['TIMING']['T_Soll1'][section-1] + (config['TIMING']['T_Soll1'][section] - config['TIMING']['T_Soll1'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0) 
        T_set[1] = config['TIMING']['T_Soll2'][section-1] + (config['TIMING']['T_Soll2'][section] - config['TIMING']['T_Soll2'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0)
        T_set[2] = config['TIMING']['T_Soll3'][section-1] + (config['TIMING']['T_Soll3'][section] - config['TIMING']['T_Soll3'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0)

    
    MFC_set[0] = config['TIMING']['MFC'][section]
    run_time = 0   
    for i in range(0,config['TIMING']['NoSections']):
        run_time += config['TIMING']['t'][i]
    t_end = run_time - (time.time() -t0)
    
    section_time = config['TIMING']['t'][0]  
    for i in range(0,section):
        section_time += config['TIMING']['t'][i]    
    t_section = section_time - (time.time() -t0)
    
    if t_section < 0:
        section +=1

    return T_set, MFC_set, t_end, section, t_section
