import py7zr
import os.path
import sys, getopt

def deploy():
    with py7zr.SevenZipFile(f'release.{sys.argv[1]}.7z', mode='w') as z:
        z.write(f"{os.path.dirname(__file__)}..\\..\\soil-moisture-sensor\\app.py", "app.py")
        z.write("iot_config.json")
        z.write("readme.md")

if __name__ == "__main__":
   deploy()