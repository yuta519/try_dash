## Try dash
Trying greate chart and data visualization library, [dash](https://dash.plotly.com/)

## Installation
```bash
python -m venv .venv
source ./.venv/bin/activate

pip install --editable ."[dev]"
```

## Run
- Single Page with simple python command
```bash
python src/examples/forecast.py
```

- Multi Page with
```bash
gunicorn src.app:server

or if the path for `gunicorn` is not set

.venv/bin/gunicorn src.app:server
```
