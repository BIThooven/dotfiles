#!/usr/bin/python

import dbus
import os
import sys

def remove_special_characters(string):
    cleaned_string = string.replace('&', '')
    return cleaned_string

try:
    bus = dbus.SessionBus()
    spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")

    if os.environ.get('BLOCK_BUTTON'):
        control_iface = dbus.Interface(spotify, 'org.mpris.MediaPlayer2.Player')
        if (os.environ['BLOCK_BUTTON'] == '1'):
            pass
        elif (os.environ['BLOCK_BUTTON'] == '2'):
            control_iface.PlayPause()
        elif (os.environ['BLOCK_BUTTON'] == '3'):
            pass

    spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
    props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    if (sys.version_info > (3, 0)):
        print(remove_special_characters(props['xesam:artist'][0]) + " - " + remove_special_characters(props['xesam:title']) + " | ")
    else:
        print(props['xesam:artist'][0] + " - " + props['xesam:title'] + " | ").encode('utf-8')
    exit
except dbus.exceptions.DBusException:
    # Write nothing
    exit
