import reflex as rx
from Python_link_bio.api.api import live, featured

USER="elbokeron"

class PageState(rx.State):

    is_live: bool
    live_title: str
    featured_info: list

    async def check_live(self):
        live_data = await live(USER)
        self.is_live = live_data["live"]
        self.live_title = live_data["title"]


    async def feature_links(self):
        self.feature_info = await featured()