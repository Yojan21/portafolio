import reflex as rx
from portafolio_python.components.link_button import link_button
from portafolio_python.components.title import title
import portafolio_python.views.constants as cons

def links() -> rx.Component:
    return rx.vstack(
        title("Redes"),
        link_button(False,
                    "LinkedIn",
                    "",
                    cons.LINKEDIN_URL,
                    cons.LINKEDIN_ICON
                    ),
        link_button(False,
                    "GitHub",
                    "",
                    cons.GITHUB_URL,
                    cons.GITHUB_ICON
                    ),
        link_button(False,
                    "Instagram",
                    "",
                    cons.INSTAGRAM_URL,
                    cons.INSTAGRAM_ICON
                    ),
        link_button(False,
                    "X",
                    "",
                    cons.X_URL,
                    cons.X_ICON
                    ),

        title("Proyectos"),
        link_button(True,
                    "Freelancer",
                    "HTML,CSS",
                    cons.FREELANCER_URL,
                    "braces"
                    ),
        link_button(True,
                    "Tienda de Ropa Dev",
                    "HTML, CSS",
                    cons.TIENDA_DE_ROPA_URL,
                    "braces"
                    ),
        link_button(True,
                    "Blog de café",
                    "HTML, CSS, JavaScript",
                    cons.BLOG_CAFE_URL,
                    "braces"
                    ),
        link_button(True,
                    "Festival de Musica",
                    "HTML, CSS, JavaScript, JSON, SCSS",
                    cons.FESTIVAL_MUSICA_URL,
                    "braces"
                    ),
        link_button(True,
                    "Portafolio",
                    "PYTHON con reflex",
                    cons.PORTAFOLIO_URL,
                    "braces"
                    ),
        width = "70%",
        color="white",
    )