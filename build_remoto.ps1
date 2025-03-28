#para correrlo en windows powerShell remoto
cd Python_link_bio
python -m venv .venv
# Activar el entorno virtual
$env:VIRTUAL_ENV = ".venv\Scripts\Activate.ps1"
. $env:VIRTUAL_ENV

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Eliminar la carpeta 'public' si existe
Remove-Item -Recurse -Force -Path "public"

# Inicializar Reflex
reflex init

# Exportar solo el frontend con Reflex
api_url=https://pruebareflex-production.up.railway.app reflex export --frontend-only

# Descomprimir el archivo 'frontend.zip' en la carpeta 'public'
Expand-Archive -Path "frontend.zip" -DestinationPath "public"

# Eliminar el archivo 'frontend.zip'
#Remove-Item -Force -Path "frontend.zip"

# Desactivar el entorno virtual
deactivate


