# Image background remover

This is a python program, which removes background from provided pictures.

## Dependances

Poetry as a package manager.
rembg library which does the trick.
The needed packages can be seen in pyproject.toml file.

## Usage

1. Download u2net pre-trained model from here: https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab
2. Put it in ~/.u2net/ folder
3. Run command "poetry install" to install required libraries
4. Run command "poetry shell" to start virtual environment
5. Run the program
6. Enter a route to the folder with initial images to be processed
7. Find pictures with removed background in ./output_pics folder
8. ...
9. PROFIT!
