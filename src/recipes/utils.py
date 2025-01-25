from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Converts a Matplotlib plot into a base64-encoded PNG image string
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

# Generates a Matplotlib chart based on specified chart type
def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG
    plt.switch_backend('AGG')

    # Specify figure size
    fig = plt.figure(figsize=(6,3))

    # Select chart type based on user input
    if chart_type == '#1':
        # Bar chart: Frequency of ingredient use across all recipes
        ingredient_counts = data['ingredients'].explode().value_counts(sort=False)

        # Filter out ingredients based on threshold
        threshold = 2
        ingredient_counts = ingredient_counts[ingredient_counts >= threshold]

        ingredient_counts.plot(kind='bar')
        plt.title('Ingredient Frequency')
        plt.xlabel('Ingredients')
        plt.ylabel('Times Used')
        plt.xticks(rotation=45, horizontalalignment='right')
    elif chart_type == '#2':
        # Pie chart: Percentage of recipes by difficulty level
        difficulty_counts = data['difficulty'].value_counts()
        difficulty_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Recipes by Difficulty')
        # Remove Y-axis label
        plt.ylabel('')
    elif chart_type == '#3':
        # Line chart: Total time for each recipe
        data.sort_values(by='name', inplace=True)
        plt.plot(data['name'], data['total_time'], marker='o', linestyle='-')
        plt.title('Recipe Total Time')
        plt.xlabel('Recipe Name')
        plt.ylabel('Total Time (minutes)')
        plt.xticks(rotation=30, horizontalalignment='right')
    else:
        print('Unknown chart type')

    # Specify layout details
    plt.tight_layout()
    # Render graph to file
    chart = get_graph()
    return chart