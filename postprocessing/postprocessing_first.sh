#!/bin/bash

### postprocessing_first.sh
### author: Hazel Leonard / hleona01
### EE 156/CS 140
### This program runs post processing python scripts for topology, cpistack,
### and mcpat in each of the output folders from the Sniper simulation.

# Path to Sniper tools
toolsPath="/h/hleona01/156/sniper-7.3/tools"

# Folder where output is stored

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
p2="ghb_prefetch"
prefs=( $p1 $p2 $p3)

cd /data/hleona01/lab2

# Access each benchmark
for i in "${benchs[@]}"
do
    cd $i
    # Access each associativity
    for j in "${assocs[@]}"
    do
        cd $j
        # Access each prefetching
        for k in "${prefs[@]}"
        do  
            cd $k
            $toolsPath/gen_topology.py
            $toolsPath/cpistack.py
            $toolsPath/mcpat.py
            cd ../
        done
        cd ../
    done
    cd ../
done
