import folium
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def foliumKorea(data,target,title):
    geo_path = './data/skorea_municipalities_geo_simple.json'
    geo_data = json.load(open(geo_path, encoding='utf-8'))

    map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
    map.choropleth(geo_data = geo_data,  
                   data = data[target],
                   columns= [data.index, data[target]],
                   fill_color= 'YlGnBu',
                   key_on='feature.id'
    )

    loc = 'Corpus Christi'
    title_html = f'''
                 <h3 align="center" style="font-size:16px"><b>{title}</b></h3>
                 '''.format(loc)   
    map.get_root().html.add_child(folium.Element(title_html))


    return map