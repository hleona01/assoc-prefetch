#!/usr/bin/env python

size = '-c big_l3'
prefix = 'splash2-'
outdir = '/data/hleona01/lab2/'
benchmarks = ['lu.cont', 'radix', 'raytrace', 'fmm', 'volrend']
assoc = ['1way', '2way', '4way', '8way',  '16way', '32way', 
                                    '64way', '128way', '256way']
#first is no prefetch
prefetch = ['no_prefetch', 'simple_prefetch', 'ghb_prefetch']

# output file: benchmark/associativity/prefetching
# part1 [outdir] part2 [benchmark] part3 [configs] part4
part1 = 'nice ./run-sniper -d '
part2 = ' -p '  
part3 = ' -i small -n 4 -c gainestown -c big_l3'
part4 = ' --roi --viz'

with open('commands.txt', 'w') as f:
    for i in benchmarks:
        for j in assoc:
            for k in prefetch:
                f.write(part1 + outdir + i + '/' + j + '/' 
                        + k + part2 + prefix + i + part3 +
                         ' -c ' + j + ' -c ' + k + part4)
                f.write('\n')