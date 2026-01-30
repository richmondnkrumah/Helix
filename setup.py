import os
import subprocess

# Create main project folder
os.makedirs("helix_agent", exist_ok=True)

# Install packages
packages = ["PySide6", "requests", "google-api-python-client", "sounddevice", "numpy"]
subprocess.run(["pip", "install", *packages])

# Optional: create subfolders for new projects
def create_project(name):
    base = os.path.join("Helix/projects", name)
    os.makedirs(base, exist_ok=True)
    os.makedirs(os.path.join(base, "src"), exist_ok=True)
    os.makedirs(os.path.join(base, "docs"), exist_ok=True)
    os.makedirs(os.path.join(base, "tests"), exist_ok=True)
    print(f"Project '{name}' created successfully.")

# Example
create_project("NutritionApp")
