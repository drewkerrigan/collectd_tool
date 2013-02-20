#collectd_tool

## About CollectdTool

CollectdTool.py is a simple script for aggregating the many files that the collectd CSV plugin generates into a single file. In order to find common ground between many different files, I've rolled up stats using a rolling average with a 1 minute window. The leftmost column on the final generated CSV file is elapsed_minutes because of this.

TODO
* Split into multiple files by group (riak, cpu, memory, etc)
* Integrate with R or another automatic graph generation technique
* Make the rolling average window configurable, as the Interval collectd config value could be > 1 minute, though not likely
* Make column names prettier and easier to read possibly through some regex magic

## Installing Collectd

### Prerequisites
yajl (Yet Another Json Library, needed for Riak Stats)
* brew install yajl
* yum install yajl
* apt-get install yajl

### Install Collectd (https://collectd.org/wiki/index.php/First_steps for more information)
* brew install collectd
* yum install collectd
* apt-get install collectd

## Setup / Start Collectd

```
git clone git://github.com/drewkerrigan/collectd_tool.git
cd collectd_tool
```

I've included a sample collectd.conf that can be used to track riak stats and a minimum of other interesting stats.

Linux
```
mv /etc/collectd/collectd.conf /etc/collectd/collectd.conf.bak
cp collectd.conf /etc/collectd/collectd.conf
/etc/init.d/collectd start
```

Mac OS X
```
sudo mkdir -p /var/lib/collectd/csv
sudo chmod 777 /var/lib/collectd/csv
collectd -C collectd.conf
```

## Stopping Collectd
Linux
```
/etc/init.d/collectd stop
```

Mac OS X
```
ps -ef | grep collectd
>   501 74052 42165   0 10:30PM ttys004    0:00.05 collectd -f -C /Users/dkerrigan/src/collectd_tool/collectd.conf
kill 74052
```

## Aggregating Statistics

```
python CollectdTool.py /var/lib/collectd/csv > stats_summary.csv
```

## Cleaning Up Statistics

```
rm -rf  /var/lib/collectd/csv/*
```