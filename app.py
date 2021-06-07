import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipe")
def get_recipe():
    recipe = list(mongo.db.recipe.find())
    return render_template("recipe.html", recipe=recipe)


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("WARNING: Username Not Available")
            return redirect(url_for("join"))

        join = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(join)

        session["user"] = request.form.get("username").lower()
        flash("Thank you for joining Kooky!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("join.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check that username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                # check that hashed password matches users input
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid user password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # invalid username or username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove session cookie from user's browser
    flash("You are now logged out of your Kooky profile")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        has_allergens = "on" if request.form.get("has_allergens") else "off"
        recipe = {
            "recipe_title": request.form.get("recipe_title"),
            "ingredients": request.form.get("ingredients"),
            "material_items": request.form.get("material_items"),
            "method": request.form.get("method"),
            "category": request.form.get("category"),
            "has_allergens": has_allergens,
            "image_link": request.form.get("image_link"),
            "submitted_by": session["user"],
            "date_submitted": request.form.get("date_submitted")
        }
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe successfully added!")
        return redirect(url_for("get_recipe"))
        
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        has_allergens = "on" if request.form.get("has_allergens") else "off"
        submit = {
            "recipe_title": request.form.get("recipe_title"),
            "ingredients": request.form.get("ingredients"),
            "material_items": request.form.get("material_items"),
            "method": request.form.get("method"),
            "category": request.form.get("category"),
            "has_allergens": has_allergens,
            "image_link": request.form.get("image_link"),
            "submitted_by": session["user"],
            "date_submitted": request.form.get("date_submitted")
        }
        mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated!")

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
