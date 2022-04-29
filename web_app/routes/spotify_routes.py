# web_app/routes/spotify_routes.py

from flask import Blueprint, request, jsonify

from app.spotify_service import artist_recommendation

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports


spotify_routes = Blueprint("spotify_routes", __name__)

@spotify_routes.route("/")
def spotify_form():
    return render_template("spotify_form.html")

@spotify_routes.route("/spotify", methods = ["POST"])
def recommend_artist():
    print("ARTIST RECOMMENDATIONS..")
    request_data = dict(request.form)  
    print("Form data:" , request_data)
    artist_name = request_data.get("artist_name") or "Taylor Swift"
    results = artist_recommendation(name = artist_name)
    print(results)
    flash("ARTIST RECOMMENDATIONS PROVIDED SUCCESSFULLY!")
    print('HEHEHEHEHEHHEHEHEHEHEHHEHEHEH')
    return render_template("spotify_results.html", results = results[0], artist_name = results[1])

if __name__ == '__main__':
   app.run()


