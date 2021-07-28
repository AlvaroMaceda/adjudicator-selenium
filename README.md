## Installation

It needs python3.6 or higher

- To install python with pyenv: `pyenv install 3.6.13`

- To create a virtual env: `virtualenv .venv --python=~/.pyenv/versions/3.6.13/bin/python3.6`
- To activate the venv: `source .venv/bin/activate`
- To deactivate: `deactivate`

## Using the filler

First of all, you need to create a file with all the centers' codes in `data.py`.
You can do it with your editor of choice (in code, for example, you can select
all the lines, press Shift+Alt+I and add the strings and the commas)

The filer is intended to automate only *part* of the work. You will need to launch
a browser and, later, attach the filler to it:

1) Launch browser:
`/opt/google/chrome/chrome --remote-debugging-port=9222 --user-data-dir='./tmp/dummy_profile'`. Update the paths accordingly to your system.
2) Navigate to the page (something like https://appweb.edu.gva.es/adjudicacio/init.do?lang=es&conv=202107590)
3) Login, and create a request. The request should be empty

After that, a very important thing to do: you should modify the styles of "add" button
using using devtools. Look for this button (the one used to add files):
```
<button type="button" class="afegir" title="Añadir fila"><img src="imgs/botons/afegir.gif" alt="Afegir fila"></button>
```
And add styles:
```
element.style {
  position: absolute;
  top: 0;
  left: 0;
}
```

If you don't do it, you will receive an error like this after some files are added:
```
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <button type="button" class="afegir" title="Añadir fila">...</button> is not clickable at point (305, 220). Other element would receive the click: <div id="t" style="display: block; top: 585.311px; left: 289px;">...</div>
```
That's caused because a hover is shown when selenium is trying to click the button.


Then, launch the script with `python filler.py`. The script should fill all the
codes in order.

**Please check everything is correct before presenting it!!**
