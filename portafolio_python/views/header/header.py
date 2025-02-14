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
                        
                ),
                rx.hstack(
                        rx.text(cons.RESUMEN,
                                color="white",
                                align="center",
                                width="100%"
                        )
                ),

                
                spacing="8",
                max_width = "90%",
                align="center",
        )
