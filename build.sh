#.\venv\Scripts\activate
#pip install --upgrade pip
#pip install -r requirements.txt
#reflex init
#reflex export --frontend-only
#Remove-Item -Path "E:\Programacion\Python\Python_link_bio\public" -Recurse -Force
#Expand-Archive -Path "frontend.zip" -DestinationPath "public"
#Remove-Item -Path "frontend.zip" -Force
#deactivate

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate


