import reflex as rx
import Python_link_bio.styles.styles as styles
import Python_link_bio.constants as const
from Python_link_bio.pages.index import index
from Python_link_bio.pages.courses import courses
from Python_link_bio.api.api import repo, live, hello



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
 head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)

app.api.add_api_route("/hello", hello)
app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)




