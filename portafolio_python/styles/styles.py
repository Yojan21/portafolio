import reflex as rx
from enum import Enum

#Constantes

MAX_WIDTH = "600px"



#Sizes

STYLESHEET =[
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;500&display=swap"
]

class Size(Enum):
    SMALL = ".5em"
    MEDIUM = ".8em"
    DEFAULT = "1.2em"
    LARGE = "1.8em"
    BIG = "2em"

class fontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"


#Styles

BASE_STYLE = {
    "background_color":"#0C151D",
    "font_weight":fontWeight.LIGHT.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value
    },
}

navbar_title_style = dict(
    font_family = "Comfortaa-Medium",
    font_weight = fontWeight.MEDIUM.value,
    font_size = Size.LARGE.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_weight="bold",
    color="white"
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_weight=fontWeight.LIGHT.value,
    color="white"
)

title_style = dict(
        width = "100%",
        padding_top = Size.DEFAULT.value
    )

