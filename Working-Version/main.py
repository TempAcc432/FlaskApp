# NOTE: When we start creating new pages, we should look into "BLOCK CONTENT" from flask for each html page, right now we are not doing that
from website import create_app
import psycopg2

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # auto reruns server