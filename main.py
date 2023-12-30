import os
import ctypes
import random

def main():

  try:
    dir_path = "C:\\Users\\Rick\\Pictures\\backgrounds"
    images = os.listdir(dir_path)
    SPI_SETDESKTOPWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, os.path.join(dir_path, random.choice(images)), 1+2)

  except IndexError as err:
    print(err)

  except FileNotFoundError as fnf_error:
    print(fnf_error)

  except Exception:
    print("Something else went wrong")

main()