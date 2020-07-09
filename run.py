from app import create_app
from app.config import Config
conf = Config()
app = create_app(conf)

if __name__ == "__main__":
    app.run()
