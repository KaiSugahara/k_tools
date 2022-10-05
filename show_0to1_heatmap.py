import plotly.express as px

def show_0to1_heatmap(arr, title=None, label_x=None, label_y=None, label_color=None, x=None, y=None):

    fig = px.imshow(arr, text_auto='.2f', aspect="auto", color_continuous_scale='gray_r', title=title, labels=dict(x=label_x, y=label_y, color=label_color), x=x, y=y)
    return fig