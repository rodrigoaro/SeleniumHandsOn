# SeleniumHandsOn

Este repo tiene un laboratorio de seleniun usando python

# Paso 0

Si usas replit modificar el archivo `replit.nix` asegurandose que contenga lo siguiente:

```
{ pkgs }: {
  deps = [
    pkgs.vim
    pkgs.python38Full
    pkgs.chromium
    pkgs.chromedriver
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}
```

Lo relevante son las lineas que dicen:

```
pkgs.chromium
pkgs.chromedriver
```

Para editar este archivo deben usar la shell de replit e instalar `nano` o `vim`.


# Paso 1

Crear un archivo `main.py` que contenga lo siguiente:

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:/google.com")
```

Luego ejecutar presionando el botón `> Run`, debería abrir la página de `google.com`.

# Paso 2

Agrega estas lineas a `main.py`

```
## Encontrar Elementos

google_text = driver.find_element(By.CLASS_NAME, "MV3Tnb").text

print(google_text)

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)
```

Presiona `> Run` y observa que ocurre.

Prueba cambiando `"selenium"` por otros valores.

# Paso 3

Agrega estas lineas a `main.py`

```
## Pausa de 5 segundos

import time

print('esperaremos 5 segundos' )
time.sleep(5)

## Volvemos a la home page

home_link = driver.find_element(By.ID, "logo")

home_link.click()

```

Observa que pasa después de presionar `> Run`.

# Paso 4

Agrega estas lineas a `main.py` y ejecutalas presionando `> Run`

```
## Buscar

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")

print(link.text)

link.click()
```

## Ejercicios

1. Modifica el script para que abra la página en Wikipeda sobre Selenium
2. Modifica el script para que abra la página web de tu organización
3. Navega en forma automatizada la página web de tu organización
4. ¿Puedes escribir un script para llenar gran aprte del formulario de esta página: https://www.selenium.dev/selenium/web/web-form.html?
