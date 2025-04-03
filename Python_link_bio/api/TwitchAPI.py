import os
import dotenv
import requests
import time

class TwitchAPI:

    dotenv.load_dotenv()
    CLIENT_ID= os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET= os.environ.get("TWITCH_CLIENT_SECRET")

    def __init__(self) -> None:
        self.token = None
        self.token_exp = 0

    def generate_token(self):
        """Genera un token de acceso para interactuar con la API de Twitch."""
        response = requests.post(
            'https://id.twitch.tv/oauth2/token',
            data={
                "client_id":self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET,
                "grant_type": "client_credentials"
            }
        )

        if response.status_code == 200:
            data = response.json()
            self.token = data["access_token"]
            self.token_exp = time.time() + data["expires_in"]
        else:
            self.token = None
            self.token_exp = 0


    def token_valid(self) -> bool:
        # Asegurarse de que self.token_exp es un número antes de hacer la comparación
        if isinstance(self.token_exp, (int, float)):
            return time.time() < self.token_exp
        else:
            return False

    def live(self, user: str) -> dict:
        """Verifica si un usuario está transmitiendo en vivo en Twitch."""
        if not self.token_valid():
            self.generate_token()

        response = requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={user}",
            headers={
                "Client-ID": self.CLIENT_ID,
                "Authorization": f"Bearer {self.token}"
            }
        )

        if response.status_code == 200 and response.json()["data"]:
            data = response.json()["data"]
            return {"live":True, "title":data[0]["title"]}

        return {"live":False, "title":""}