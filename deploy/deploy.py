import py7zr
import os.path
import sys, getopt

def deploy():
    with py7zr.SevenZipFile(f'release.{sys.argv[1]}.7z', mode='w') as z:
        wdir = os.path.dirname(__file__)
        topDir = os.path.dirname(wdir)

        z.write(f"{os.path.join(topDir, 'soil-moisture-sensor/app.py')}", "app.py")
        z.write("iot_config.json")
        z.write("readme.md")

if __name__ == "__main__":
   deploy()