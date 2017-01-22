#from flask import Flask, request
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/profile/<first_name>.<last_name>')
def profile(first_name, last_name):
    return render_template('profile.html', f_name=first_name, l_name=last_name)

if __name__ == '__main__':
    app.run()
