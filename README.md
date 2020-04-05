# location-updater
MacOS has location settings, that allow you to alter your IP configuration, like custom DNS or static IP settings.
This script changes that location setting based on the Wifi name (SSID) you connect to.

For now it only handles 1 location based on a list of SSIDs.

# Prerequisites
In the file preferences.json you specify the name of your location and add the list of matching SSIDs.

If the current Wifi name matches any of the specified SSIDs, it will switch to that location and enforce its (custom) settings.

e.g.
```
{
    "macos_location": "Home",
    "home_networks": ["firstwifi", "secondwifi", "otherwifi"]
}
```
Add an entry in your crontab.   In this example, it runs every 10 minutes and logs to a hidden folder .log in the user home.
```
*/10 * * * * /usr/local/bin/python3 /my/script/location/loc_update.py >> ~/.log/location-update.log 2>&1
```

# [ todo ]
* dict with SSIDs  and their corresponding location
* add vpn capability
