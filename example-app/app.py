from shiny import Inputs, Outputs, Session, App, render, ui
import pandas as pd
import numpy as np
import asyncio
from loading_spinners import with_spinner


app_ui = ui.page_fluid(
    ui.input_slider("rows", "Rows", 0, 100, 20),
    with_spinner(ui.output_data_frame("result")),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.data_frame
    async def result():
        await asyncio.sleep(2)
        return pd.DataFrame(
            np.random.randint(0, 100, size=(input.rows(), 4)), columns=list("ABCD")
        )


app = App(app_ui, server)
