from flask import Flask, render_template, request
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html.j2')

@app.route('/pokedex', methods=['GET', 'POST'])
def pokedex():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if not response.ok:
            error_string = "We have no idea what happened, but its an error"
            return render_template('pokedex.html.j2', error= error_string)
        if not response.json()["forms"][0]["name"]:
            error_string = "Dude learn your Pokemon."
            return render_template('pokedex.html.j2', error= error_string)
        data = response.json()
        pokedex=[]
        for poke in data:
            poke_dict={
                "nameplate": poke["forms"][0]["name"],
                "1_ability": poke["abilities"][0]["ability"]["name"],
                "defense": poke["stats"][2]["base_stat"],
                "attack": poke["stats"][1]["base_stat"],
                "hp": poke["stats"][0]["base_stat"],
                "7up": poke["sprites"]["front_shiny"]
            }
            pokedex.append(poke_dict)
        return render_template('pokedex.html.j2', poke=pokedex)
    return render_template('pokedex.html.j2')


#need to establish a search in /pokedex for users to input their pokemon and retrieve data back
# use ergast.html.j2 as a reference