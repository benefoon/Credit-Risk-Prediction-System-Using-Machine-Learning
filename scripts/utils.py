import os

def ensure_directories_exist(directories):
    """Ensure that required directories exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

if __name__ == "__main__":
    # Ensure necessary directories are created
    dirs = ["data/raw", "data/processed", "models", "scripts"]
    ensure_directories_exist(dirs)
    print("Required directories created.")
