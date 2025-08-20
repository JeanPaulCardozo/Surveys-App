# surveys_app

Este proyecto es una aplicación web desarrollada con Django para gestionar encuestas.

## Requisitos
- Python 3.10 o superior
- pip
- Entorno virtual recomendado (venv)

## Instalación

1. Clona el repositorio o descarga el proyecto en tu máquina.
2. Accede al directorio del proyecto:
   ```powershell
   cd C:\Users\HP\Downloads\surveys_venv\surveys_app
   ```
3. Crea y activa un entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
   Si no existe `requirements.txt`, instala Django y python-dotenv manualmente:
   ```powershell
   pip install django python-dotenv
   ```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto para variables de entorno
2. Configura la base de datos en `mysite/settings.py` si deseas usar otra distinta a SQLite.

## Migraciones

Crea las migraciones:
```powershell
python manage.py makemigrations
```

Luego ejecuta las migraciones para preparar la base de datos:
```powershell
python manage.py migrate
```

## Ejecución del servidor

Inicia el servidor de desarrollo:
```powershell
python manage.py runserver
```
Accede a la aplicación en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso

- La app principal es `polls`, donde puedes crear y votar en encuestas.
- Las plantillas HTML se encuentran en `polls/templates/polls/`.
- Para acceder a la app, visita `/polls/` en el navegador.

## Pruebas

Para ejecutar las pruebas:
```powershell
python manage.py test polls
```

## Estructura del proyecto

```
surveys_app/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── polls/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── polls/
│   │       ├── index.html
│   │       ├── detail.html
│   │       └── results.html
│   └── ...
```

## Notas
- Modifica el archivo `.env` y `settings.py` según tus necesidades.
- Para producción, desactiva el modo debug y configura los hosts permitidos
