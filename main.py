import subprocess
import sys
import os
import time
from time import sleep
import psutil
import win32api


def get_drives():
    unidades = subprocess.getoutput("fsutil fsinfo drives").split(" ")[1:]
    last_drive = unidades[-1]
    len_drives = unidades.index(last_drive)

    return len_drives + 1


while True:
    for controlador in range(0, get_drives()):
        try:
            removable = psutil.disk_partitions()[controlador][3].split(",")[1]

            if "removable" in removable:
                USB_nombre = psutil.disk_partitions()[controlador][1]
                USB_etiqueta = win32api.GetVolumeInformation(f"{USB_nombre}\\")[
                    0]

                if USB_etiqueta == "KINGSTON":
                    print("Dispositivo detectado -> :" + str(USB_etiqueta))
                    sys.exit()

        except IndexError:
            pass

    sleep(1)
