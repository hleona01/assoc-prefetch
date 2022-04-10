#!/bin/bash

### lab2_setup.sh
### author: Hazel Leonard / hleona01
### EE 156/CS 140
### This program sets up directories and Sniper experiments using five
### benchmarks with varying LLC associativity and prefetchers.
### This file should be placed in the sniper 7.3 folder

# Associativities: 1-way (direct mapped), 2-way, 4-way, 8-way, 16-way 
# 32-way, 64-way, 128-way, 256-way (fully associative for 16384 cache)

# Define variables
# Main folder to store output
lab2_folder="/data/hleona01/lab2"

# Names of benchmarks
b1="lu.cont"
b2="radix"
b3="raytrace"
b4="fmm"
b5="volrend"
benchs=( $b1 $b2 $b3 $b4 $b5)

# Associativities
r1="1way"
r2="2way"
r3="4way"
r4="8way"
r5="16way"
r6="32way"
r7="64way"
r8="128way"
r9="256way"
assocs=( $r1 $r2 $r3 $r4 $r5 $r6 $r7 $r8 $r9)

# Prefetching
p1="no_prefetch"
p2="simple_prefetch"
p3="ghb_prefetch"
prefs=( $p1 $p2 $p3)

cd benchmarks

# Create a directory for benchmarks in lab1 folder
for i in "${benchs[@]}"
do
    mkdir -p $lab2_folder/$i
    # Make sub-directories for associativity
    for j in "${assocs[@]}"
    do
        mkdir -p $lab2_folder/$i/$j
        # Make sub-directories for prefetching
        for k in "${prefs[@]}"
        do
            mkdir -p $lab2_folder/$i/$j/$k
        done
    done
done


# Run sniper on each benchmark with 3 different L2 cache sizes
parallel < ../lab2_commands.txt

echo "scripts done"

# Check if sim.out is created
for i in "${benchs[@]}"
do
    for j in "${assocs[@]}"
    do
        for k in "${prefs[@]}"
        do
            test -f $lab2_folder/$i/$j/$k/sim.out || echo "$k in $j in $i does not exist."
        done
    done
done
