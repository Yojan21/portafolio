import reflex as rx
from portafolio_python.styles.styles import Size as Size
import portafolio_python.views.constants as cons

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(
                                src="/perfil.jpg",
                                alt="Foto de perfil",
                                size="8",
                                border="5px solid #4299E1"
                                ),
                        rx.vstack(
                                rx.heading(
                                        "Hola, mi nombre es Yojan Romero",
                                        color="white",
                                        size="5"
                                ),
                                rx.link(
                                        rx.text(
                                                "@yojanromero",
                                                margin_top = "0px !important",
                                                color="white"
                                        ),
                                        href=cons.GITHUB_URL,
                                        is_external="True",
                                ),
                                rx.text(
                                        "Colombia",
                                        margin_top = "0px !important",
                                        color="white",
                                ),
                                align_items = "start",
                                margin_left = Size.DEFAULT.value
                        ),
                        align="center"
                ),
                rx.text(
                        """Soy Ingeniero Electrónico con experiencia en desarrollo de sistemas electrónicos,
                        robótica y desarrollo web. Competente en herramientas como MATLAB, ROS,
                        Python y diseño de circuitos electrónicos. Apasionado por resolver problemas
                        complejos con innovación tecnológica.""",
                        color="white"
                        ),
                spacing="8",
                max_width = "90%",
                justify="center"
        )
