import flet as ft
import time
import smi2sublist as ss

wid=750
hig=400

def main(page: ft.Page):
    page.title="E.S.P.ER."
    page.padding=0
    page.bgcolor = ft.colors.BLACK

    def begin_play(e):
        now.value=""
        #now.value=page.width
        page.update()
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

    title=ft.Text("E.S.P.ER.", size=20, weight=ft.FontWeight.BOLD)
    filename=ft.TextField(label="path")
    play=ft.ElevatedButton(text="PLAY", on_click=begin_play)

    now=ft.Text("NO SUBTITLES",
                color=ft.colors.WHITE,
                size = 30,
                text_align=ft.TextAlign.CENTER)
    
    set_compo = ft.Column(
        controls=[title, filename, play,],
        alignment=ft.alignment.center

    )

    settings=ft.Container(
        width=wid/4,
        height=hig,
        margin=ft.margin.all(0),
        padding=20,
        content=set_compo,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
    )

    printer=ft.Container(
        width=wid,
        height=hig,
        margin=ft.margin.all(0),
        padding=50,
        content=now,
        alignment=ft.alignment.top_center,
        bgcolor=ft.colors.BLACK,
    )

    all=ft.Container(
        width=wid,
        height=hig,
        padding=0,
        content=ft.Row(
            spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            controls=[settings,printer,],
        ),
        bgcolor=ft.colors.BLACK,
    )

    page.add(all)
    page.update()

ft.app(main)