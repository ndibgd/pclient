# run.py

import os
# from project import app
from flask import app

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
