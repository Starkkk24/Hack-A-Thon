from app import create_app
from datetime import datetime, timedelta

app = create_app()
app.permanent_session_lifetime = timedelta(days=7)  #

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
