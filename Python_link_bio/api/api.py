import Python_link_bio.constants as const
from Python_link_bio.api.TwitchAPI import TwitchAPI
from Python_link_bio.api.SupabaseAPI import SupabaseAPI


TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()

async def hello()-> str:
    return "Minoldo-Aldo"

async def repo()-> str:
    return const.REPO_URL

async def live(user : str)-> dict:
    return TWITCH_API.live(user)

async def featured()-> list:
    return SUPABASE_API.featured()