A ui wrapper for adding a css loading spinner to a shiny app.

## Usage

```python
from loading_spinners import with_spinner

app_ui = ui.page_fluid(
    ui.input_slider("rows", "Rows", 0, 100, 20),
    with_spinner(ui.output_data_frame("result")),
)
...
```

## Using/ Developing package

### Setting up python package in "editable" mode

This should be run from the root of the repo

```
pip install -e .
```

## Running the example app

If you want to run the example app from the command line you can run:

```
Shiny run example-app/app.py
```
