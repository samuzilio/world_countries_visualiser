from flask import Flask, render_template
import folium

# Create a Flask app
app = Flask(__name__)

# Create a Folium map
m = folium.Map(
    max_bounds=True,
    tiles=None,
    control_scale=True,
    zoom_start=3,
    location=[45.0, 10.0]
)

# Add basemap tile layer
folium.TileLayer(
    tiles="https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    control=False,
    max_zoom=20,
    subdomains="abcd",
    no_wrap=True
).add_to(m)

# Define a style function for GeoJSON layer
region_color_mapping = {
    "Africa": "#e41a1c",
    "Americas": "#377eb8",
    "Antarctica": "#e8e9eb",
    "Asia": "#4daf4a",
    "Europe": "#984ea3",
    "Oceania": "#ff7f00"
}
def style_function(feature):
    region = feature["properties"]["region_un"]
    fill_color = region_color_mapping.get(region)
    return {
        "fillColor": fill_color,
        "fillOpacity": 0.40,
        "color": "white",
        "weight": 1.00
    }

# Add GeoJSON layer with style and tooltip
political_countries_url = ("http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson")
folium.GeoJson(
    political_countries_url,
    style_function=style_function,
    highlight_function=lambda x: {
        "fillOpacity": 1
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["name"],
        labels=False,
        style="""
        font-family: Space Mono, monospace;
        font-size: 15px;
        font-weight: 800;
        color: #404040;
        border: 1px solid black
        """
    )
).add_to(m)

# Save the map to an HTML file
m.save("templates/map.html")

# Define a route for rendering the map
@app.route("/")
def test():
    return render_template("layout.html")

if __name__ == '__main__':
    app.run(debug=True)
