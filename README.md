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

# [ todo ]
* dict with SSIDs  and their corresponding location
* add vpn capability
