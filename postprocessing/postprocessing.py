#!/usr/bin/env python

### postprocessing.py
### author: Hazel Leonard / hleona01
### EE 156/CS 140
### This program extracts data obtained from Sniper experiments
### and exports it to a CSV file.

import os
import csv

# Variables
benchs = ['cholesky', 'fmm', 'lu.cont', 'radix', 'raytrace']
assoc = ['1way', '2way', '4way', '8way', '16way', '32way', '64way',
                                                 '128way', '256way']
prefetch = ['ghb_prefetch', 'no_prefetch', 'simple_prefetch']

# Extraction function definitions:
# Extract average miss rate from sim.out
def extractMissRate():
    with open("sim.out","r") as sim:
        # if line starts with IPC, get the core0 stat
        for line in sim:
            if line.startswith("  Cache L3"):
                for line in sim:
                    if 'miss rate' in line:
                        parts = line.split("|")
                        core0 = parts[1].strip()
                        core1 = parts[2].strip()
                        core2 = parts[3].strip()
                        core3 = parts[4].strip()
                        core0 = core0[:-1]
                        core1 = core1[:-1]
                        core2 = core2[:-1]
                        core3 = core3[:-1]
                        data = (float(core0) + float(core1) +
                                float(core2) + float(core3)) / 4
                        return data

# Extract average core IPC from sim.out
def extractIPC():
    with open("sim.out","r") as sim:
        # if line starts with IPC, get the core0 stat
        for line in sim:
            if line.startswith("  IPC"):
                parts = line.split("|")
                core0 = parts[1].strip()
                core1 = parts[2].strip()
                core2 = parts[3].strip()
                core3 = parts[4].strip()
                data = (float(core0) + float(core1) +
                        float(core2) + float(core3)) / 4
                return data

# Extract Peak Dynamic Power of L3 cache from power.txt
def extractL3Power():
    with open("power.txt", "r") as power: 
        # get info from the first L2 section
        for line in power:
            if line.startswith("      L3"):
                for line in power: 
                    if 'Peak Dynamic' in line:
                        parts = line.split("=")
                        data = parts[1].strip()
                        return data

# Generate miss rate CSV
def generateCSV(cols, csv_name, extract_func):
    # Make CSV
    f = open(csv_name, 'w')
    writer = csv.writer(f)
    writer.writerow(cols)
    # Add Miss Rate data 
    for i in benchs:
        os.chdir(i)
        for j in assoc:
            os.chdir(j)
            currLine = []
            for k in prefetch:
                os.chdir(k)
                print(os.getcwd())
                # Write benchmark
                currLine.append(i)
                # Write associativity
                currLine.append(j)
                # Write prefetcher
                currLine.append(k)
                # get miss rate
                currLine.append(extract_func())
                writer.writerow(currLine)
                currLine = []
                os.chdir("..")
            os.chdir("..")
        os.chdir("..")
    
    f.close()

# Needed for each: cols, csv name, extract function
mr_cols = ['Benchmark','Associativity','Prefetcher','Miss Rate (%)']
ipc_cols = ['Benchmark','Associativity','Prefetcher','IPC']
pow_cols = ['Benchmark','Associativity','Prefetcher','Power']

generateCSV(mr_cols, 'missrate.csv', extractMissRate)
generateCSV(ipc_cols, 'ipc.csv', extractIPC)
generateCSV(pow_cols, 'pow.csv', extractL3Power)