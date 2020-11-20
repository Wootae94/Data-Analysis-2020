from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (37.565956,126.800760)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')
def markerr():
    df = pd.read_csv('brand_cafe_kangseo.csv')
    color_dict = {'Clear' : 'blue', 'Snow': 'white', 'Rain':'gray','Extreme':'red','Clouds':'orange','Mist':'green'}
    mapping = folium.Map(location=[37.565956,126.800760], zoom_start=13)
    for i in df.index:
        folium.Marker(
        location=[df['위도'][i],df['경도'][i]], 
        popup= df['상호명'][i],
        tooltip = f'{df.desc[i]}, {df.temp[i]}',
        icon=folium.Icon(color = df.color[i],icon=df.icon[i])
    ).add_to(mapping)

    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)