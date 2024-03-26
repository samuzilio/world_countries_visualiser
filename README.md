# World Countries Visualiser
This repository contains a simple [Flask](https://flask.palletsprojects.com/en/3.0.x/) application to visualise Natural Earth's *de facto* [boundaries of world countries](http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson) using [Folium](https://python-visualization.github.io/folium/latest/#) library.

![screenshot](https://github.com/samuzilio/world_countries_visualiser/assets/94171193/c305ca4b-417c-4de6-8ff2-aee1e2ab1ebf)

<br>

## Instructions
Follow these steps to set up and run the app on your local machine:

**1**. Clone the repository:
```
$ git clone https://github.com/samuzilio/world_countries_visualiser.git
```
**2**. Launch your text editor;

**3**. Open the cloned repository;

**4**. Start a new terminal;

**5**. Create and activate a virtual environment:
```
$ python -m venv .venv
```
```
$ .venv\Scripts\activate (for Windows)
$ source .venv/bin/activate (for macOS and Linux)
```
**6**. Install dependencies:
```
$ pip install -r requirements.txt
```
**7**. Run the application:
```
$ python app.py
```
And then head to http://127.0.0.1:5000/ in your browser!
