import plotly.graph_objects as go
import pandas as pd


pd.options.plotting.backend = "plotly"


user_template = dict(
    layout=go.Layout(title_font=dict(family="Arial", size=24))
)

config = {
    'scrollZoom': True,
    'toImageButtonOptions': {
        'format': 'png',  # one of png, svg, jpeg, webp
        'filename': 'graphx_img',
        'height': 768,
        'width': 1024,
        'scale': 1
    },
    'modeBarButtonsToRemove': [
        'zoom',
        'zoomIn',
        'zoomOut',
        'resetScale',
        'lasso2d',
        'select'
    ],
    'displaylogo': False
}
df = pd.read_csv("csv_tbl.csv", delimiter=';')

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df.Time,
        y=df.Value,
        mode='lines',
        name='График',
        line=dict(
            color='red',
            width=5,
            shape='spline'
        )
    )
)
fig.update_layout(
    title="Пример построения графика",
    template=user_template,
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(0, 0, 0)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(0, 0, 0)',
        ),
        tickcolor='rgb(0, 0, 0)',
        ticklen=5


    ),
    yaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(0, 0, 0)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(0, 0, 0)'
        ),
        tickcolor='rgb(0, 0, 0)',
        ticklen=5

    ),
    autosize=True,
    margin=dict(
        autoexpand=False,
        l=100,
        r=100,
        t=110
    ),
    showlegend=True,
    legend=dict(
        x=1.01,
        y=1,
        traceorder="reversed",
        title_font_family="Courier",
        font=dict(
            family="Consolas",
            size=12,
            color="black"
        ),
        bgcolor="white",
        bordercolor="Black",
        borderwidth=0
    ),
    plot_bgcolor='rgb(245, 245, 245)',
    legend_title_text='Легенда'
)
fig.show(config=config)
