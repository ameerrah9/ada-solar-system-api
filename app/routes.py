from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

# # Create a list of `Planet` instances
# planets = [
#     Planet(1, "Mercury", "Smallest planet", 0),
#     Planet(2, "Venus", "Second brightest object in the sky", 0),
#     Planet(3, "Earth", "Only planet known to support life", 1),
#     Planet(4, "Mars", "Red planet", 2),
#     Planet(5, "Jupiter", "Largest planet", 79),
#     Planet(6, "Saturn", "Second largest planet", 82),
#     Planet(7, "Uranus", "Third largest planet", 27),
#     Planet(8, "Neptune", "Fourth largest planet", 14),
#     Planet(9, "Pluto", "Not a planet", 5)
# ]

# Create a `planets_bp` Blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# # Define a route for the `planets_bp` Blueprint
# @planets_bp.route("", methods=["GET"])
# # Define a function that returns a list of all planets
# # get all existing `planets`
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "moons": planet.moons
#         })
#     return jsonify(planets_response)

# # validate a planet helper function
# def validate_planet(planet_id):
#     # validate planet_id is an integer
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     # if planet_id is not found, return 404
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# define a route for a single planet resource
# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "moons": planet.moons
#     }

# define a route for creating a planet resource
@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons,
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons,
        }
    else:
        abort(404)
        
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.moons = form_data["moons"]
        db.session.commit()

        return make_response(f"planet #{planet.id} successfully updated")
    else:
        abort(404)
        
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"planet #{planet.id} successfully deleted")
    else:
        abort(404)

