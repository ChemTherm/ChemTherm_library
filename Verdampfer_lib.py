#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def json_timing(config, section, t0):
    T_set = [0,0,0]
    MFC_set = [0]
    
    T_set[0] = config['TIMING']['T_Soll1'][section-1] + (config['TIMING']['T_Soll1'][section] - config['TIMING']['T_Soll1'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0) 
    T_set[1] = config['TIMING']['T_Soll2'][section-1] + (config['TIMING']['T_Soll2'][section] - config['TIMING']['T_Soll2'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0)
    T_set[2] = config['TIMING']['T_Soll3'][section-1] + (config['TIMING']['T_Soll3'][section] - config['TIMING']['T_Soll3'][section-1]) / (config['TIMING']['t'][section] ) * (time.time() - t0)
    
    MFC_set[0] = config['TIMING']['MFC'][section]
    return T_set, MFC_set
