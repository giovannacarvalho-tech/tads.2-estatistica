import plotly.express as px
from plotly.graph_objects import Figure
from download import download_data


def plot_ts(ticker:str) -> Figure:
    df = download_data(ticker)
    fig = px.line(df,
        x='Date',
        y='Close',
        title=f'{ticker} Stock Price')
   
    return fig
