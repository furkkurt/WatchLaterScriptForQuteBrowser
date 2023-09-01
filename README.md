<h1>
  Huh?
</h1>
I was getting a little frustrated with youtube's watch later playlist so I created this little script that stores your watch later list as a text file to later play the list in mpv.

<h1>
  Installation:
</h1>


Put the watchLater.sh and watchLater.txt to .config/qutebrowser/userscripts/  
Put these key bindings to .config/qutebrowser/config.py  
```
config.bind("wl", "spawn bash -c 'echo {url} >> ~/.config/qutebrowser/userscripts/watchLater.txt'")  
config.bind("wr", "spawn bash -c 'grep -v {url} ~/.config/qutebrowser/userscripts/watchLater.txt >> tmp.txt && mv tmp.txt ~/.config/qutebrowser/userscripts/watchLater.txt'")  
config.bind("wp", "spawn bash -c 'mpv $(~/.config/qutebrowser/userscripts/watchLater.sh)'")
```
<h1>
  Usage
</h1>
Open the youtube video and press wl to add to watch later and wr to remove from watch later.  
Press wp to play your watch later list
