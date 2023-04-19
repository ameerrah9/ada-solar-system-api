from flask import Blueprint, jsonify

# Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

# Create a list of `Planet` instances
planets = [
    Planet(1, "Mercury", "Smallest planet", 0),
    Planet(2, "Venus", "Second brightest object in the sky", 0),
    Planet(3, "Earth", "Only planet known to support life", 1),
    Planet(4, "Mars", "Red planet", 2),
    Planet(5, "Jupiter", "Largest planet", 79),
    Planet(6, "Saturn", "Second largest planet", 82),
    Planet(7, "Uranus", "Third largest planet", 27),
    Planet(8, "Neptune", "Fourth largest planet", 14),
    Planet(9, "Pluto", "Not a planet", 5)
]

# Create a `planets_bp` Blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# Define a route for the `planets_bp` Blueprint
@planets_bp.route("", methods=["GET"])
# Define a function that returns a list of all planets
# get all existing `planets`
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(planets_response)

# define a route for a single planet resource
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons
            }