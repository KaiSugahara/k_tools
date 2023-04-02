from IPython.display import display, HTML

def print_hr(**style):

    style.setdefault("margin", "2em 0")
    style.setdefault("border", "0.2em solid lightblue")
    
    style = "".join([f"{key}: {val};" for key, val in style.items()])
    
    display(HTML(f'<hr style="{style}">'))