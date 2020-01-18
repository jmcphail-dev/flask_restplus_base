"""
This script is intended for development use only and is not suitable for running Flask in a production environment
"""
from app import create_app

def run():
    app = create_app()
    app.run()


if __name__ == "__main__":
    run()
