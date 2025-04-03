import reflex as rx
from enum import Enum

# from Python_link_bio.components.navbar import navbar
from Python_link_bio.styles.colors import Color
from Python_link_bio.styles.colors import TextColor
from Python_link_bio.styles.fonts import Font, FontWeight

#Constans
MAX_WIDTH = "600px"

#Creo un array
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "/css/styles.css"
]

#Sizes -tamaños
class Size(Enum):
    ZERO = "0"
    SMALL = "5"
    MEDIUM = "2"
    DEFAULT = "1"
    BIG = "8"
    LARGE = "26px"
    SUPERBIG = "50px"
    VERY_BIG = "9"

#Styles
BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT,
    "background_color":Color.BACKGROUND.value,

    # rx.Heading: {
    #   "color": TextColor.HEADER.value,
    #     "font_family": Font.TITLE.value,
    #     "font_weight": FontWeight.MEDIUM.value
    # },
    rx.button:{
        "widht":"100%",
        "height":"100%",
        # "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "word_break": "break-all",#hace responsivo el texto del boton
        "text_align": "start",
        "_hover":{
            "background_color":Color.SECONDARY.value
        },
        "background_color": Color.CONTENT.value
        # "align_items":"center",
        # "justify_content":"center"
    },
    rx.link:{
        "text_decoration":"none",#quita subrayado
        "_hover":{}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    size="7",
    width="100%",
    font_family=Font.TITLE.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)