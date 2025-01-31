import reflex as rx
from portafolio_python.styles.styles import Size as Size
import portafolio_python.views.constants as cons

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(
                                src="/perfil.jpg",
                                size="8",
                                border="5px solid #4299E1"
                                ),
                        rx.vstack(
                                rx.heading(
                                        "Hola, mi nombre es Yojan Romero",
                                        size="5"
                                ),
                                rx.link(
                                        rx.text(
                                                "@yojanromero",
                                                margin_top = "0px !important",
                                        ),
                                        href=cons.GITHUB_URL,
                                        is_external="True",
                                ),
                                rx.text(
                                        "Colombia"
                                ),
                                align_items = "start",
                                margin_left = Size.DEFAULT.value,
                                margin_top = Size.DEFAULT.value
                        )
                ),
                rx.text("""Soy Ingeniero Electrónico con experiencia en desarrollo de sistemas electrónicos,
                        robótica y desarrollo web. Competente en herramientas como MATLAB, ROS,
                        Python y diseño de circuitos electrónicos. Apasionado por resolver problemas
                        complejos con innovación tecnológica."""),
                spacing="8",
        )
