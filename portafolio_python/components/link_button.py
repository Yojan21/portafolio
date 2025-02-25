import reflex as rx
import portafolio_python.styles.styles as styles
from portafolio_python.styles.styles import Size as Size

def link_button(estado:bool, text:str, body:str, url:str, etq:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag = etq,
                    width = Size.DEFAULT.value,
                    height = Size.DEFAULT.value,
                    alt="Imagen icono"
                ),
                rx.vstack(
                    rx.text(
                        text,
                        style=styles.button_title_style
                        ),
                    rx.cond(
                        estado,
                        rx.text(
                            body,
                            style=styles.button_body_style
                            ),
                    ),
                    spacing="0",
                ),
                align="center",
                margin = Size.MEDIUM.value,
                padding_left = ".5em"
            ),
        ),
        href=url,
        is_external="True",
        width="100%"
    )