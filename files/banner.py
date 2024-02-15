import os
from rgbprint import gradient_print
import platform

logo = f"""
          _           _       _                    _    
__      _(_)_ __   __| | ___ | |__  _ __ ___  __ _| | __
\ \ /\ / / | '_ \ / _` |/ _ \| '_ \| '__/ _ \/ _` | |/ /
 \ V  V /| | | | | (_| | (_) | |_) | | |  __/ (_| |   < 
  \_/\_/ |_|_| |_|\__,_|\___/|_.__/|_|  \___|\__,_|_|\_\
                                                        
            Author: Sajadtlpr | Hitlos Security Team    (V 0.0.1)
      =============================================================
                      [+] Twitter @sajadtlpr
                      [+] Instagram @sajadtlpr                          
      =============================================================
"""




def banner():
    gradient_print(logo , start_color='cyan' , end_color='yellow')


def clear():
    os.system("cls") if 'Windows' in platform.platform() else os.system("clear")
