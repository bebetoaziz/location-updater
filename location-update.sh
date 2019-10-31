#!/bin/sh

#get the ssid of the network you are on
#shown on two lines; should be one with a space
ssid=`ioreg -l -n AirPortDriver | grep APCurrentSSID | sed 's/^.*= "\(.*\)".*$/\1/; s/ /_/g'`
#fill in your own values for ssid and location below
if [ $ssid="demlem" ]
then
    location="Home-DNS"
 elif [ $ssid = "telenet-5E84E" ]
 then
     location="Home-DNS"
# elif [ $ssid = "friend" ]
# then
#     location="Joe"
else
    location="Automatic"
fi

#update the location
newloc=`/usr/sbin/scselect ${location} | sed 's/^.*(\(.*\)).*$/\1/'`
#echo ${newloc}

#exit with error if the location didn't match what you expected
if [ ${location} != ${newloc} ]
then
    exit 1
fi

exit 0
logger -i -p daemon.notice -t set-hostname setting location to "${location}"
