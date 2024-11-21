import flet as ft
from src.config import AppConfig

def text(text: str, style: str, color: str) -> ft.Text:
    return ft.Text(
        value = text, 
        size = AppConfig.TEXT_STYLES[style]["size"],
        weight = AppConfig.TEXT_STYLES[style]["weight"], 
        font_family = AppConfig.TEXT_STYLES[style]["font_family"],
        color = AppConfig.COLORS[color]
    )

def image(image_src: str, width: int = 20) -> ft.Image:
    return ft.Image(
        src = AppConfig.ICONS[image_src], 
        fit = ft.ImageFit.CONTAIN, 
        width = width
    )

def row_image_text(image_src: str, text_: str, style: str, color: str) -> ft.Row:
    return ft.Row(
        controls = [
            image(image_src), 
            text(text_, style, color)
        ], 
        alignment = "start",
        spacing = 10
    )

def title(text: str) -> ft.Container:
    return ft.Container(
        content=row_image_text("bullet_title", text, "title", "bbva_aqua"),
    )


def subtitle(text: str) -> ft.Container:
    return ft.Container(
        content=row_image_text("bullet_subtitle", text, "subtitle", "bbva_medium_blue"),
    )

def button(text: str, on_click: callable) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        text = text,
        on_click = lambda e: on_click(e),
        width = 250,
        height = 35,
        bgcolor = AppConfig.COLORS["bbva_core_light_blue"],
        color = AppConfig.COLORS["bbva_white"],
        style = ft.ButtonStyle(
            shape = ft.RoundedRectangleBorder(radius=0),
            padding = ft.padding.symmetric(horizontal=10, vertical=10),
        ),
    )

def separator() -> ft.Container:
    return ft.Container(
        height = 1,
        bgcolor = AppConfig.COLORS["bbva_light_gray"],
    )

