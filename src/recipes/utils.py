from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    # Create a BytesIO buffer for the image
    buffer = BytesIO()

    # Create a plot with BytesIO object as a file-like object, set format to png
    plt.savefig(buffer, format='png')

    # Set cursor to beginning of the stream
    buffer.seek(0)

    # Retrieve the content of the file
    image_png = buffer.getvalue()

    # Encode the bytes-like object
    graph = base64.b64encode(image_png)

    # Decode to get the string as output
    graph = graph.decode('utf-8')

    # Free up memory of buffer
    buffer.close()

    # Return the image/graph
    return graph

def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG
    plt.switch_backend('AGG')

    # Specify figure size
    fig = plt.figure(figsize=(6,3))

    # Select chart type based on user input
    if chart_type == '#1':
        # X-axis ingredients names
        # Y-axis frequency of ingredient use across all recipes
    elif chart_type == '#2':
        # Show what percentage of recipes fall into each difficulty level
    elif chart_type == '#3':
        # X-axis Recipe name
        # Y-axis Total time in minutes
    else:
        print('Unknown chart type')

    # Specify layout details
    plt.tight_layout()
    # Render graph to file
    chart = get_graph()
    return chart