# wallpaper-cycle
A simple program that cycles through wallpapers. Supporting only X11 using feh.

## Dependencies
- python
- feh

## Usage
### On startup (~/.xinitrc)
```sh
python /path/to/cycle.py -t 300 -p ~/Wallpapers &
exec your_wm
```

### Options
```
-h    shows this help message
-p    the directory in which the wallpapers are located
-t    the time between each change (in seconds)
-r    shuffle all wallpapers randomly
```
