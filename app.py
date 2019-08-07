from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin,  login_required, login_user, logout_user
import pandas as pd
app = Flask(__name__)

# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        # self.name = name #"user" + str(id)
        # self.password =password# self.name + "_secret"

    def set_user_psswd(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20
#users = [User(id) for id in range(1, 21)]

users={'squadra1': 'passwd1', 'squadra2': 'passwd2', 'squadra3': 'passwd3', 'squadra4': 'passwd4', 'squadra5': 'passwd5' \
       , 'squadra6': 'passwd6', 'squadra7': 'passwd7', 'squadra8': 'passwd8', 'squadra9': 'passwd9', 'squadra10': 'passwd10',\
     'squadra11': 'passwd11', 'squadra12': 'passwd12', 'squadra13': 'passwd13', 'squadra14': 'passwd14', 'squadra15': 'passwd15',\
     'squadra16': 'passwd16', 'squadra17': 'passwd17', 'squadra18': 'passwd18', 'squadra19': 'passwd19', 'squadra20': 'passwd20'}

# users={('squadra1', 'passwd1'), ('squadra2', 'passwd2'), ('squadra3', 'passwd3'), ('squadra4', 'passwd4'), ('squadra5', 'passwd5') \
#        , ('squadra6', 'passwd6'), ('squadra7', 'passwd7'), ('squadra8', 'passwd8'), ('squadra9', 'passwd9'), ('squadra10', 'passwd10')\
#         ,   ('squadra11', 'passwd11'), ('squadra12', 'passwd12'), ('squadra13' ,'passwd13'), ('squadra14', 'passwd14'), ('squadra15', 'passwd15'),\
#        ('squadra16', 'passwd16'), ('squadra17', 'passwd17'), ('squadra18', 'passwd18'), ('squadra19', 'passwd19'), ('squadra20', 'passwd20')}
print(users["squadra1"])
# some protected url
@app.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        if request.form['action'] == 'Start':
            return redirect(url_for('login'))



    else:

        return render_template('home.html')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #if users.__contains__(username):
            #print(users[username])
        if users.__contains__(username) and password == users[username]:
            id = username.split('squadra')[1]

            user = User(id)
            user.set_user_psswd(username, password)
            login_user(user)
            return redirect(url_for('enigma1'))
        else:
            return abort(401)
    else:
        return render_template('login.html')



@app.route("/Enigma1", methods=["GET", "POST"])
@login_required
def enigma1():
    # if not session.get('logged_in'):
    #     return render_template('login.html')
    # else:
    session['sblocco_enigma2'] = False
    if request.method == 'POST':
        if request.form['action'] == 'tabella':
            return redirect(url_for('show_tables'))
        password = request.form['password_en']

        if password == "ciao":
            session['sblocco_enigma2'] = True
            #session['logged_in_2'] = True
            if request.form['action'] == 'Submit':
                return redirect(url_for('enigma2'))
            # return redirect(request.args.get("next"))
        else:

            return abort(401)
    else:

        return render_template('Enigma1.html')



@app.route("/Enigma2", methods=["GET", "POST"])
@login_required
def enigma2():
    if not session.get('sblocco_enigma2'):
        return abort(401)
        #return render_template('login.html')
    else:
    #
    #     session['logged_in_2'] = False
        session['sblocco_enigma3'] = False
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
            password = request.form['password_en']

            if password == "ciao":
                session['sblocco_enigma3'] = True
                #session['logged_in_2'] = True
                if request.form['action'] == 'Submit':
                    return redirect(url_for('enigma3'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma2.html')

@app.route("/Enigma3", methods=["GET", "POST"])
@login_required
def enigma3():
    if not session.get('sblocco_enigma3'):
        return abort(401)
    else:
        session['sblocco_enigma4'] = False
    #     session['logged_in_2'] = False
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
            password = request.form['password_en']

            if password == "ciao":
                session['sblocco_enigma4'] = True
                #session['logged_in_2'] = True
                if request.form['action'] == 'Submit':
                    #return Response("Hello World!")
                    return redirect(url_for('enigma4'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma3.html')

@app.route("/Enigma4", methods=["GET", "POST"])
@login_required
def enigma4():
    if not session.get('sblocco_enigma4'):
        return abort(401)
    else:
        session['sblocco_enigma5'] = False
    #     session['logged_in_2'] = False
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
            password = request.form['password_en']

            if password == "ciao":
                session['sblocco_enigma5'] = True
                #session['logged_in_2'] = True
                if request.form['action'] == 'Submit':
                    #return Response("Hello World!")
                    return redirect(url_for('enigma5'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma4.html')


@app.route("/Enigma5", methods=["GET", "POST"])
@login_required
def enigma5():
    if not session.get('sblocco_enigma5'):
        return abort(401)
    else:
        session['sblocco_enigma6'] = False
    #     session['logged_in_2'] = False
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
            password = request.form['password_en']

            if password == "ciao":
                session['sblocco_enigma6'] = True
                #session['logged_in_2'] = True
                if request.form['action'] == 'Submit':
                    #return Response("Hello World!")
                    return redirect(url_for('enigma6'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma5.html')

@app.route("/Enigma6", methods=["GET", "POST"])
@login_required
def enigma6():
    if not session.get('sblocco_enigma6'):
        return abort(401)
    else:
        session['sblocco_enigma7'] = False
    #     session['logged_in_2'] = False
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
            password = request.form['password_en']

            if password == "ciao":
                session['sblocco_enigma7'] = True
                #session['logged_in_2'] = True
                if request.form['action'] == 'Submit':
                    #return Response("Hello World!")
                    return redirect(url_for('enigma7'))
                # return redirect(request.args.get("next"))
            else:

                return abort(401)
        else:

            return render_template('Enigma6.html')


@app.route("/Enigma7", methods=["GET", "POST"])
@login_required
def enigma7():
    if not session.get('sblocco_enigma7'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            if request.form['action'] == 'tabella':
                return redirect(url_for('show_tables'))
        return render_template('Enigma7.html')



# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route("/showtable")
@login_required
def show_tables():

    url2 = "https://docs.google.com/spreadsheets/d/1Ctwd5GOLggDZgRA3I5irQewttQw-a6XCqGHsmYDnnqE/export?format=csv"
    # s=requests.get(url).content
    data = pd.read_csv(url2)

    data.set_index(['Nome Squadra'], inplace=True)
    data.index.name = None


    return render_template('view.html', tables=[data.to_html(classes='tab_cluedo')],
                           # , males.to_html(classes='male')],
                           titles=['na', 'Situazione squadre'])


if __name__ == "__main__":
    app.run()