#!/usr/bin/env python
import os, sys, csv, glob, re, time, math

def get_stat_name(filename):    #host  group  stat yyyy  mm   dd
    matchObj = re.match( r'(.*)\/(.*)\/(.*)-(.*)-(.*)-(.*)', filename, re.M|re.I)
    if matchObj:
        group = matchObj.group(2)
        stat = matchObj.group(3)
        return group + "." + stat
    else:
        return filename
    
def build_stats(stats_dict, filename):
    name = get_stat_name(filename)
    first_ts = -1
            
    with open(filename, 'rb') as summary_file:
        reader = csv.reader(summary_file)
        reader.next()

        for row in reader:
            row = map(str.strip, row)
            vals = map(float, row)
            
            if first_ts == -1:
                first_ts = vals[0]
            
            ts = vals[0]
            tdm = math.floor((ts - first_ts) / 60)
            
            if "bytes" in name or "memory" in name:
                vals[1] = vals[1] / 1048576
            
            if tdm in stats_dict.keys():
                if name in stats_dict[tdm].keys():
                    r_avg = stats_dict[tdm][name]
                    stats_dict[tdm][name] = ((r_avg + vals[1]) / 2)
                else:
                    stats_dict[tdm][name] = vals[1]
            else:
                stats_dict[tdm] = {}
                stats_dict[tdm][name] = vals[1]
            
    return stats_dict

stats_dict = {}

for stat_file in glob.glob(sys.argv[1] + '/*/*/*'):
    stats_dict = build_stats(stats_dict, stat_file)

key_order = sorted(stats_dict.itervalues().next().keys())
print "elapsed_minutes," + ','.join(key_order)
for ts in stats_dict:
    print str(ts) + ',' + ','.join([str(stats_dict[ts][key]) for key in key_order])