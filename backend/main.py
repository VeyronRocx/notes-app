import os
from app import app

if __name__ == "__main__":
    # Use PORT environment variable if it exists, otherwise default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Set host to 0.0.0.0 to make the server publicly available
    app.run(host="0.0.0.0", port=port)
