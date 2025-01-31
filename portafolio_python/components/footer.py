import reflex as rx
import datetime
from portafolio_python.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/logo_azul.jpg",
                alt="Logotipo de Yojan Romero",
                width="70px",
                height="70px",
                border_radius = Size.SMALL.value
                ),
            rx.link(
                f"2022-{datetime.date.today().year} YOJAN ROMERO V1.",
                href="https://www.linkedin.com/in/yojanromero/",
                is_external=True,
                font_size=Size.MEDIUM.value,
                color="blue"
            ),
            rx.text(
                "INGENIERO ELECTRÓNICO/DESARROLLADOR WEB",
                font_size=Size.MEDIUM.value,
                margin_top = "0px !important",
                color="white"
                ),
            margin_bottom = Size.BIG.value,
            align_items = "center"
            ),
    )