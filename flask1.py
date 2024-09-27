from flask import *
import random
app= Flask(__name__)



@app.route('/')
def homepage():
    return render_template('cheems.html', com_name="Microsoft")

app.run(host='0.0.0.0', debug=True)

