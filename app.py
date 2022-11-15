from flask import Flask, jsonify
from flask_cors import CORS

from models.super_hero import SuperHero

app = Flask(__name__)
CORS(app)


@app.route('/api/super-heroes', methods=['GET'])
def get_super_heroes():
    batman = SuperHero("Batman", "Conocimiento científico")
    superman = SuperHero("Superman", "Fuerza sobrehumana y capacidad para volar")
    aquaman = SuperHero("Aquaman", "Dominación psiónica de la vida marina")
    mujer_maravilla = SuperHero("Mujer Maravilla", "Superhumana y domino de armas")

    super_heroes = [
        batman,
        superman,
        aquaman,
        mujer_maravilla
    ]

    return jsonify([hero.serialize() for hero in super_heroes])


## Other example
@app.route('/api/super-heroes2', methods=['GET'])
def get_super_heroes_2():
    batman = {
        "name": "Batman",
        "skill": "Conocimineto cientifico"
    }

    superman = {
        "name": "Superman",
        "skill": "Fuerza superhumana y capacidad para volar"
    }

    super_heroes = [
        batman,
        superman
    ]

    return super_heroes


if __name__ == '__main__':
    app.run()
