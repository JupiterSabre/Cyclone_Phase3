# Run this file to run webservefrom website import create_app
from Website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) 