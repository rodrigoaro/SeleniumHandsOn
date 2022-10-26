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


# Paso 1:

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


