from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the main marketing page."""
    return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    """Handles the hero section email subscription form."""
    # In a real application, you would save the email to a database
    # or a mailing list service here.
    email = request.form.get("email")
    print(f"New subscription from: {email}") # Server-side log
    # Return a success response to the client
    return jsonify({"message": "Thank you for subscribing!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=10000)

