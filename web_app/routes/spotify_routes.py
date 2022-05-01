# web_app/routes/spotify_routes.py

from flask import Blueprint, request, jsonify

from app.spotify_service import artist_recommendation

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports

spotify_routes = Blueprint("spotify_routes", __name__)

#displays the spotify form page 
@spotify_routes.route("/")
def spotify_form():
    return render_template("spotify_form.html")

#display the recommended artists and songs if user puts in an inputted artist
@spotify_routes.route("/spotify", methods = ["POST"])
def recommend_artist():
    request_data = dict(request.form)  
    artist_name = request_data.get("artist_name") or "Dua Lipa"
    results = artist_recommendation(name = artist_name)
    if results is None:
        flash("There are no results for your inputted artist. Please try again.")
        return render_template("spotify_form.html")
    else:
        print("ARTIST RECOMMENDATIONS..")
        print("Form data:" , request_data)
        print(results)
        flash("Artist Recommendations Provided Successfully!")
        return render_template("spotify_results.html", results = results[0], artist_name = results[1])

#displays the about page
@spotify_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")


if __name__ == '__main__':
   app.run()


