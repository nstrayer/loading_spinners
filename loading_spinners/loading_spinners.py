from pathlib import PurePath

from htmltools import HTMLDependency, div


# This object is used to let Shiny know where the dependencies needed to run
# our component all live. In this case, we're just using a single javascript
# file but we could also include CSS.
loading_spinners_deps = HTMLDependency(
    "loading_spinners",
    "1.0.0",
    source={
        "package": "loading_spinners",
        "subdir": str(PurePath(__file__).parent),
    },
    stylesheet={"href": "spinner.css"},
)


def with_spinner(*args):
    return div(
        {"class": "spinner-wrapper"},
        loading_spinners_deps,
        *args,
        div({"class": "spinner"})
    )
