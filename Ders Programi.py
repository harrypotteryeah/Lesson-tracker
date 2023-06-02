import subprocess
import pyautogui
import keyboard
import win32con
import win32gui
import datetime

ders_listesi=[("","tde","mat","mat","cls"),("","","mat","mat","kmy","kmy","alm","alm"),("kmy","")]
ders_saatleri=[(8,15),(9,5),(9,55),(10,45),(11,35),(13,5),(13,55),(14,45)]
cuma_ders_saatleri=[(8,15),(9,5),(9,55),(10,45),(11,35),(13,5),(13,55),(14,45)]
now=datetime.datetime.now()
suanki_ders=None
with open("son_ders.txt","r+")as f:
    son_ders=f.read()

saatler=ders_saatleri if now.day!=5 else cuma_ders_saatleri

for i,zaman in enumerate(saatler):
    if now.hour == zaman[0]:
        if i<len(saatler)-1:
            if now.minute >= zaman[1] and not (now.hour==saatler[i+1][0] and now.minute<saatler[i+1][1]): 
                suanki_ders=ders_listesi[now.weekday][i]


def open_window(dosya:str,classname):
    subprocess.Popen([dosya])
    wind=win32gui.FindWindow(classname,None)
    if wind==0:
        raise Exception("Window not found")
    win32gui.SetWindowPos(wind, win32con.HWND_TOPMOST, 100, 100, 300, 200, 0) 
    win32gui.ShowWindow(wind, win32con.SW_MAXIMIZE)

if __name__=="__main__":
    if son_ders!=suanki_ders:
        with open("son_ders.txt","w+") as f:
            f.write(suanki_ders)
        
        if suanki_ders=="mat":
            pass
        elif suanki_ders=="tde":
            pass
        elif suanki_ders=="fzk":
            pass
        elif suanki_ders=="kmy":
            pass
        elif suanki_ders=="ing":
            pass
        elif suanki_ders=="byj":
            pass
        elif suanki_ders=="din":
            pass    
        elif suanki_ders=="alm":
            pass
        elif suanki_ders=="cls":
            pass