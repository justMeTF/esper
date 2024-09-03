import flet as ft
import time
import smi2sublist as ss

def main(page: ft.Page):

    def begin_play(e):
        pre=0
        sub=ss.smi2sub(filename.value)
        for i in range(len(sub)):
            try:
                time.sleep(sub[i][0]-pre)
                now.value=sub[i][1]
                page.update()
                time.sleep(sub[i+1][0]-sub[i][0])
                pre=sub[i+1][0]
            except:
                pass
    
    now=ft.Text()
    filename=ft.TextField(label="smi file path")
    play=ft.ElevatedButton(text="PLAY", on_click=begin_play)
    page.add(now,filename,play)
    page.update()
    
    
ft.app(main)