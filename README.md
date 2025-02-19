# README

Para poder usar está plantilla para la documentación del proyecto deberemos preparar nuestro entorno de trabajo. Vamos a realizar la siguientes instalaciones:

- [Python](https://www.python.org/downloads/). Es importante activar la opción en el instalador `Add Python.exe to PATH`. 
- [Visual Studio Code](https://code.visualstudio.com/download).

En visual studio code, presionamos `Ctrl + J` para abrir el terminal, instalamos virtualenv con el siguiente comando:

```bash
pip install virtualenv
```

Creamos un ambiente virtual, en el ejemplo lo cree en la ruta `C:\venv\mkdocs``, pero pueden usar cualquier ruta. 

```bash
python -m venv C:\venv\mkdocs
```

Y activamos luego, el ambiente virtual (el ejemplo es para windows):

```bash
C:\venv\mkdocs\Scripts\Activate.ps1  
```

Abrimos la carpeta donde crearas la documentación (`Ctrl + K` seguido de `Ctrl + O`). 

Y estando allí, en el terminal: Activamos el ambiente virtual  e instalamos los requerimientos. 

```bash
C:\venv\mkdocs\Scripts\Activate.ps1  
pip install -r .\requirements.txt
```

## Mkdocs Serve

```bash
C:\venv\mkdocs\Scripts\Activate.ps1  
mkdocs serve
```
## GitHub pages
```bash
C:\venv\mkdocs\Scripts\Activate.ps1  
mkdocs gh-deploy
```