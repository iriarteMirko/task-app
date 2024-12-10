import flet as ft
from src.config import AppConfig


def text(text: str, color: str|None = None, style: str = "body") -> ft.Text:
    return ft.Text(
        value = text, 
        color = AppConfig.COLORS[color] if color else None,
        size = AppConfig.TEXT_STYLES[style]["size"],
        weight = AppConfig.TEXT_STYLES[style]["weight"], 
        font_family = AppConfig.TEXT_STYLES[style]["font_family"],
    )

def image(image_src: str, width: int = 20) -> ft.Image:
    return ft.Image(
        src = AppConfig.ICONS[image_src], 
        fit = ft.ImageFit.CONTAIN, 
        width = width
    )

def row_image_text(text_: str, image_src: str, color: str|None = None, style: str = "body", alignment: str|ft.Alignment = "start") -> ft.Row:
    return ft.Row(
        controls = [
            image(image_src), 
            text(text_, color, style)
        ], 
        alignment = alignment,
        spacing = 0 if text_ == "" else 10,
    )

def title(text: str, imagen_src: str = "bullet_title", color: str = "bbva_aqua") -> ft.Container:
    return ft.Container(
        content = row_image_text(text, imagen_src, color, "title"),
    )

def subtitle(text: str, imagen_src: str = "bullet_subtitle", color: str = "bbva_medium_blue") -> ft.Container:
    return ft.Container(
        content = row_image_text(text, imagen_src, color, "subtitle"),
    )

def button(content: str, on_click: callable, width: int = 250, height: int = 35, bgcolor: str|None = "bbva_core_light_blue") -> ft.ElevatedButton:
    return ft.ElevatedButton(
        content = ft.Text(content) if isinstance(content, str) else content,
        on_click = lambda e: on_click(e),
        width = width,
        height = height,
        bgcolor = AppConfig.COLORS[bgcolor] if bgcolor else None,
        color = AppConfig.COLORS["bbva_white"],
        style = ft.ButtonStyle(
            shape = ft.RoundedRectangleBorder(radius=0),
            padding = ft.padding.symmetric(horizontal=10, vertical=10),
            overlay_color={"hovered": AppConfig.COLORS["bbva_core_blue"]},
            visual_density = ft.VisualDensity.COMFORTABLE,
            mouse_cursor = "pointer",
        ),
    )

def separator() -> ft.Container:
    return ft.Container(
        height = 1,
        bgcolor = AppConfig.COLORS["bbva_light_gray"],
    )
