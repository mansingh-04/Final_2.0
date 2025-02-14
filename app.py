import os
import sys
import shutil
import webbrowser
import threading
from flask import Flask, render_template, request

# Adjust the template and static path for the bundled app
template_folder = os.path.join(sys._MEIPASS, 'templates') if hasattr(sys, '_MEIPASS') else 'templates'
static_folder = os.path.join(sys._MEIPASS, 'static') if hasattr(sys, '_MEIPASS') else 'static'

# Initialize Flask app with correct paths for templates and static
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path) or filename.startswith("."):
            continue  

        file_extension = filename.split(".")[-1].lower()
        
        if file_extension:
            subfolder_name = f"{file_extension.upper()} Files"
            subfolder_path = os.path.join(folder_path, subfolder_name)

            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

            new_file_path = os.path.join(subfolder_path, filename)

            if os.path.exists(new_file_path):
                base_name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(new_file_path):
                    new_filename = f"{base_name}_{counter}{ext}"
                    new_file_path = os.path.join(subfolder_path, new_filename)
                    counter += 1
            
            shutil.move(file_path, new_file_path)
            print(f"Moved: {filename} -> {subfolder_name}/")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        folder_path = request.form["folder_path"]
        if os.path.isdir(folder_path):
            clean_folder(folder_path)
            return render_template("index.html", message="Cleaning Completed!")
        else:
            return render_template("index.html", message="Please provide a valid folder path.")
    return render_template("index.html")

# Open browser automatically after starting Flask server
  # Opens Flask app in default browser

if __name__ == "__main__":
    def open_browser():
        webbrowser.open("http://127.0.0.1:5000")
    # Start the Flask server and open the browser after a slight delay
    threading.Timer(1.5, open_browser).start()
    app.run(debug=False)

