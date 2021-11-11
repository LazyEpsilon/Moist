import py7zr
import os.path
import sys, getopt

def deploy():
    with py7zr.SevenZipFile(f'release.{sys.argv[1]}.7z', mode='w') as z:
        wdir = os.path.dirname(__file__)
        topDir = os.path.dirname(wdir)

        z.write(f"{os.path.join(topDir, 'soil_moisture_sensor/app.py')}", "app.py")
        z.write(f"{os.path.join(wdir, 'iot_config.json')}")
        z.write(f"{os.path.join(wdir, 'readme.md')}")

if __name__ == "__main__":
   deploy()