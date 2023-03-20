#Nombre del archivo app.py
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from forms import FormVideoGame
app = Flask(__name__, template_folder='template')
app.secret_key='cl4v3#S3cr3t4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/video-games.db'
db = SQLAlchemy(app)

class Video_Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=False)
    image = db.Column(db.String(100),unique=False,nullable=False)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/video-games/", methods=["GET"])
@app.route("/video-games/<int:id>", methods=["GET"])
def video_games(id = None):
    if id:
        return f'Video juego con id {id}'
    else:
        list_video_games=Video_Game.query.all()
        return render_template("video-games.html", list_video_games=list_video_games)

@app.route("/video-games/new", methods=["GET","POST"])
def new_video_game():
    form = FormVideoGame()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(app.root_path+"/static/img/"+filename)

        video_game = Video_Game(title=title,description=description,image=filename)
        db.session.add(video_game)
        db.session.commit()

        return render_template("video-game-added.html",title=title)
    else:
        return render_template("video_game_wtf.jinja2",form=form)
    

@app.route("/about-us", methods=["GET"])
def about_us():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error = "Page not found..."), 404
if __name__ == '__main__':
    app.run(debug=True)