import flet as ft
import time
import smi2sublist as ss

def main(page: ft.Page):
    page.title="E.S.P.ER."
    page.padding=0
    page.window.width=600
    page.window.height=270
    page.bgcolor = ft.colors.GREY_900

    page.window.frameless=True
    page.window.center()

    #page.vertical_alignment=ft.alignment.center
    #page.horizontal_alignment=ft.alignment.center
    #page.window.full_screen=True
    #page.theme = ft.Theme(color_scheme_seed="black")

    def begin_play(e):
        now.value=""
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
                size = 20,
                #theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
                text_align=ft.TextAlign.CENTER)
    
    set_compo = ft.Column(
        controls=[title, filename, play,],
        alignment=ft.alignment.center

    )
    settings=ft.Container(
        margin=ft.margin.all(0),
        padding=20,
        width=200,
        height=270,
        content=set_compo,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
    )

    printer=ft.Container(
        margin=ft.margin.all(0),
        padding=50,
        width=600,
        height=270,
        content=now,
        alignment=ft.alignment.top_center,
        bgcolor=ft.colors.BLACK,
    )

    page.add(
        ft.Row(
            width=600,
            spacing=0,
            scroll=ft.ScrollMode.ALWAYS,
            controls=[settings,printer,],
        )
    )
    page.update()
    
ft.app(main)