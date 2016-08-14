# -- encoding: UTF-8 --
import json

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [float(p["longitude"]), float(p["latitude"])]},
            "properties": {"title": p["name"]},
        } for p in (json.load(open("pizza-online.json", encoding="utf-8")))
    ]
}

with open("pizzaonline.geojson", "w", encoding="utf-8") as outfp:
    json.dump(geojson, outfp)
