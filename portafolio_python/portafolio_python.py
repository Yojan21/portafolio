import reflex as rx
from portafolio_python.components.navbar import navbar
from portafolio_python.components.footer import footer
from portafolio_python.views.header.header import header
from portafolio_python.views.links.links import links
import portafolio_python.styles.styles as styles

""" class State(rx.State):
    pass """

def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                align_items="center"
            )   
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEET,
    style=styles.BASE_STYLE
)
app.add_page(index)
app._compile()