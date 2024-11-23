import flet as ft
from src.components.components import title


class Profile:
    def __init__(self, content_area):
        self.content_area = content_area
        self.container = ft.Container(
            content = title("Mi perfil"),
        )
    
    def load_profile(self):
        """Carga el contenido de la sección 'Perfil' en el área dinámica."""
        self.content_area.container.content = self.container
        self.content_area.container.update()
