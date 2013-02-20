#collectd_tool

## Installing Collectd

### Prerequisites
* yajl (Yet Another Json Library, needed for Riak Stats)
** brew install yajl
** yum install yajl
** apt-get install yajl

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