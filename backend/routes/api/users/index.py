"""Index page for the User API."""
from flask import jsonify, Response

from backend.models import User
from backend.route import Route


class UserIndex(Route):
    """Index class for the User API."""

    name = "index"
    path = "/"

    @staticmethod
    def get() -> Response:
        """GET request to the User index."""

        # Create a list to store our result
        data = []

        # Query the database for all users
        for instance in User.query.order_by(User.id):
            # Convert the instance to a dictionary
            d = instance.__dict__
            # Get rid of the state key since it cannot be serialised to JSON
            d.pop("_sa_instance_state")

            # Get rid of the password key for security
            d.pop("password")
            d["type"] = d.pop("type").value

            # Add it to the temporary list
            data.append(d)

        # Return a JSON copy of the database quuery
        return jsonify(data)
