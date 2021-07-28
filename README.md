It needs python3.6 or higher

- To install python with pyenv: `pyenv install 3.6.13`

- To create a virtual env: `virtualenv .venv --python=~/.pyenv/versions/3.6.13/bin/python3.6`
- To activate the venv: `source .venv/bin/activate`
- To deactivate: `deactivate`


USE THIS APPROACH:
- Launc browser: `/opt/google/chrome/chrome --remote-debugging-port=9222 --user-data-dir='./tmp/dummy_profile'`
- Login and navigate to the request
- Launch python to add the requests: `python test2.py`

- Attaching:
https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/
`/opt/google/chrome/chrome --remote-debugging-port=9222 --user-data-dir='./tmp/dummy_profile'`
To check it's working: http://127.0.0.1:9222/ from a normal browser
