import reflex as rx
import portafolio_python.styles.styles as styles
from portafolio_python.styles.styles import Size as Size

def navbar()-> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                rx.text.strong("Yojan Romero Ariza"),
                style = styles.navbar_title_style
            ),
        ),
        position="stricky",
        font_weigth = "bold",
        color="white",
        border_radius = Size.SMALL.value,
        background_color="#4299E1",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )