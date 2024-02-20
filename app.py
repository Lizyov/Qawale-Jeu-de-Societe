from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import Flask, redirect, url_for
import logging
from enum import Enum
from home.main import *
from time import *
import random
from flask import jsonify

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)


app = Flask(__name__)

qawale_game = start_game_main("Qawale", ["Joueur1", "Joueur2"])
#qawale_game = start_game_main("Quarto", ["Joueur1", "Joueur2"])

@app.route('/')
def main():

    return render_template('home/index.html')

@app.route('/index')
def index():

    return render_template('home/index.html')

@app.route('/project')
def project():
    return render_template('home/project.html')

@app.route('/rules')
def rules():
    return render_template('home/rules.html')

@app.route('/rulesQuarto')
def rulesQuarto():
    return render_template('home/rulesQuarto.html')

@app.route('/rulesQawale')
def rulesQawale():
    return render_template('home/rulesQawale.html')

@app.route('/choixJoueurs/<game>')
def choixJoueurs(game):
    app.logger.info(game)
    return render_template('home/choixJoueurs.html', game=game)

@app.route('/startGame/<game>/<player1>/<player2>')
def start_game(game, player1, player2):

    app.logger.info(player1 + " ; " + player2)

    global qawale_game
    
    qawale_game = start_game_main(game, [player1, player2])

    return {}

@app.route('/end')
def end():

    winner = None

    if qawale_game.players[0].alignments > qawale_game.players[1].alignments:

        winner = qawale_game.players[0].name

    if qawale_game.players[1].alignments > qawale_game.players[0].alignments:

        winner = qawale_game.players[1].name
    
    return render_template('home/end.html', game=qawale_game, winner=winner)

@app.route('/plate')
def plate():
    return render_template('home/game/plate.html', plate=qawale_game.board, game=qawale_game)

@app.route('/plate2')
def plate2():
    return render_template('home/game/plate2.html')

@app.route('/select_case/<x>/<y>')
def select_case(x, y):

    app.logger.info(f"Case selectionnée : {x} {y}")

    return qawale_game.select_case(x, y)

@app.route('/select_galet/<id>')
def select_galet(id):

    app.logger.info(f"Galet sélectionné : {id}")

    return qawale_game.select_pawn(int(id))

@app.route('/click_quarto_button/<id_player>')
def click_quarto_button(id_player):

    app.logger.info(f"Un joueur a cliqué sur un bouton QUARTO : {id_player}")

    if isinstance(qawale_game.board, QuartoBoard):

        return qawale_game.board.quarto_button_click(id_player, qawale_game.players)
    
    return {}


@app.route('/get_updated_plateau')
def get_updated_plateau():
   
    for player in qawale_game.players: 
        if player.his_turn: player.played_time+=1

    b = qawale_game.need_update
    if b: qawale_game.need_update = False

    return {"plate":qawale_game.board.to_json(), "game":qawale_game.to_json(), "translation":qawale_game.board.translation_grid, "plate_has_to_change":b}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3669)
