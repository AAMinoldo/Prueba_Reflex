import reflex as rx
from Python_link_bio.styles.colors import Color
import Python_link_bio.constants as constants

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.Component]
    href: rx.Var[str]
    href=constants.COFFEE_URL#paso directamente hasta encontrar el problema
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}



# Creación del botón flotante
float_button = FloatButton.create

