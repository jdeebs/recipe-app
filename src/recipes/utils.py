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