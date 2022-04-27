# web_app/routes/spotify_routes.py

from flask import Blueprint, request, jsonify

from app.spotify_service import artist_recommendation

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports

spotify_routes = Blueprint("spotify_routes", __name__)

@spotify_routes.route("/spotify")
def recommend_artist():
    print("ARTIST RECOMMENDATIONS..")
    request_data = dict(request.args)
    name = request_data.get("name")
    results = artist_recommendation(name = name)
    flash("ARTIST RECOMMENDATIONS PROVIDED SUCCESSFULLY!")
    return render_template("spotify.html")

if __name__ == '__main__':
   app.run()


#@spotify_routes.route("/api/spotify.json")
#def weather_forecast_api():
   # print("WEATHER FORECAST (API)...")
   # print("URL PARAMS:", dict(request.args))
#
#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
#    if results:
#        return jsonify(results)
#    else:
#        return jsonify({"message":"Invalid Geography. Please try again."}), 404
#
#@weather_routes.route("/weather/form")
#def weather_form():
#    print("WEATHER FORM...")
#    return render_template("weather_form.html")
#
#@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
#def weather_forecast():
#    print("WEATHER FORECAST...")
#
#    if request.method == "GET":
#        print("URL PARAMS:", dict(request.args))
#        request_data = dict(request.args)
#    elif request.method == "POST": # the form will send a POST
#        print("FORM DATA:", dict(request.form))
#        request_data = dict(request.form)
#
#    country_code = request_data.get("country_code") or "US"
#    zip_code = request_data.get("zip_code") or "20057"
#
#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
#    if results:
#        flash("Weather Forecast Generated Successfully!", "success")
#        return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)
#    else:
#        flash("Geography Error. Please try again!", "danger")
#        return redirect("/weather/form")