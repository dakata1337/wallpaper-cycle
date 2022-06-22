import sys, getopt
import subprocess
import random
import time
import os

__relfile__=os.path.basename(__file__)
IMAGE_FORMATS = ("jpeg", "jpg", "png", "webp")

def bold(string: str) -> str:
    return f"\x1b[1m{string}\x1b[0m"

def usage():
    print(f"""\
{__relfile__} version 0.1
Usage: {__relfile__} -t [TIMEOUT] -p [PATH]
  {bold('-h')}\t shows this help message
  {bold('-p')}\t the directory in which the wallpapers are located
  {bold('-t')}\t the time between each change
  {bold('-r')}\t shuffle all wallpapers randomly""")
    sys.exit(0)

def change_wallpaper(wp_path: str):
    subprocess.run(["/usr/bin/feh", "--bg-scale", wp_path])

def iteration(root: str, files: list, timeout: int):
    for _ in range(len(files)):
        file = files.pop()
        change_wallpaper(f"{root}/{file}")
        time.sleep(timeout)

def file_filter(file: str) -> bool:
    return file.endswith(IMAGE_FORMATS)

def main():
    opts, _ = getopt.getopt(sys.argv[1:], "hp:t:r")

    path: str = ""
    timeout: int = 300
    is_random = False
    for arg, val in opts:
        if arg == "-h":
            usage()
        elif arg == "-p":
            path = val
        elif arg == "-t":
            timeout = int(val)
        elif arg == "-r":
            is_random = True

    if len(path) == 0:
        print("Path option is required! Use -h for more info.")
        sys.exit(1)

    while True:
        files = list(filter(file_filter, os.listdir(path)))
        if is_random: random.shuffle(files)

        iteration(path, files, timeout)

if __name__ == "__main__":
    main()

