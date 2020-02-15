# VICREO Listener (Linux)
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">

*Hotkey listener for LINUX*

This fork makes available a CLI-only version of Vicreo, for linux machines. No toolbar app.
[Click here to go to the original, up-to-date branch.](https://github.com/JeffreyDavidsz/VICREO-Listener)

Go to [VICREO releases](https://github.com/JeffreyDavidsz/VICREO-Listener/releases) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to perform hotkey actions from remote clients.

[<img src="https://bitfocus.io/companion/badge.png?ref=vicreo" width="200px" alt="Controllable by Companion">](https://bitfocus.io/companion/)

## Installation (Linux)

To control foreground apps on linux, from another computer, via companion:

On linux listener (receiving commands):
* Install python and pipenv. 
* Download this code repo (and unzip if necessary).
* Navigate into the folder containing this code, in the terminal. Run these commands:
* `$ pipenv install -r requirements.txt`

On client machine (the one you are sending commands from):
* Connect to the same local network as listener machine
* Open bitfocus companion
* Before clicking "launch GUI": Choose LAN port instead of localhost (perhaps "en0:...")
* In companion GUI, under connections/instances, add vicreo hotkey instance
* In instance config, set IP address to match vicreo listener IP ("Listening ... at xxx.xxx.xxx.xxx)

## Usage

In the linux terminal, navigate to vicreo listener code folder and type:
* `$ pipenv shell`
* `$ python vicreo_listener_linux.py`
to launch listener.

Enter ip address in companion vicreo config. You should be set.

## Modifiers ##

>The following modifier are supported:

alt
ctrl
tab
shift
cmd
alt_gr
delete
backspace
space
caps_lock
end
enter
esc
f1
f2
f3
f4
f5
f6
f7
f8
f9
f10
f11
f12
home
insert (only windows)
left
right
up
down
num_lock (only windows)
page_up
page_down