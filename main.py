import flet as ft
from src.app import TaskApp


def main(page: ft.Page):
    TaskApp(page)

if __name__ == "__main__":
    ft.app(target=main)