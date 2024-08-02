from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import webcolors
import os

app = Flask(__name__)

def rgb_to_hex(rgb):
    return webcolors.rgb_to_hex(rgb)

def find_average_colors(image_path, n_colors=3):
    # Load image
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure image is in RGB format
    pixels = np.array(image)

    # Reshape the image to a 2D array of pixels
    pixels = pixels.reshape(-1, 3)

    # Use KMeans to find clusters of colors
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)
    
    # Get the cluster centers (average colors)
    average_colors = kmeans.cluster_centers_.astype(int)
    
    colors = []
    for color in average_colors:
        hex_color = rgb_to_hex(tuple(color))
        rgb_color = f"rgb({color[0]}, {color[1]}, {color[2]})"
        colors.append({"hex": hex_color, "rgb": rgb_color})
    
    return colors

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    num_colors = int(request.form.get('numColors', 3))
    if not (3 <= num_colors <= 10):
        return jsonify({"error": "Number of colors must be between 3 and 10"}), 400
    
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    colors = find_average_colors(file_path, num_colors)
    
    return jsonify({"colors": colors})

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
