#%%
import geopandas as gpd
import folium
import streamlit as st

st.set_page_config(layout='centered') #centered or wide
header_container = st.beta_container()

with header_container:
    st.header('Mapa de incidentes de piratería marítima, usando el índice H3 de Uber.')
    st.subheader('Carlos HG - galaviz@outlook.com')

    data_gpd = gpd.read_file('gridcounts.gpkg')
	
    m = folium.Map(location=[21.593073, 10.800750], zoom_start=2, tiles='cartodb dark_matter')
    myscale = (0, 5, 10, 20, 30, 100, 200, 400)

    folium.Choropleth(
        geo_data=data_gpd,
        name='choropleth',
        data=data_gpd,
        columns=['h3', 'count'],
        key_on='feature.properties.h3',
        fill_color='OrRd',
        fill_opacity=0.5,
        line_opacity=0.2,
        threshold_scale=myscale,
        legend_name='Cuenta ASAMs',
        highlight_function=lambda x: {'weight':3, 'color':'black', 'fillOpacity':1},    
        tooltip=folium.features.GeoJsonTooltip(fields=['count'], aliases=['Count:'])
    ).add_to(m)

    style_function = lambda x: {'fillColor': '#ffffff', 'color':'#000000', 'fillOpacity': 0.1, 'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 'color':'#000000', 'fillOpacity': 0.50, 'weight': 0.1}

    data_style = folium.features.GeoJson(
        data_gpd,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['count'],
            aliases=['Count: '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
        )
    )

    m.add_child(data_style)
    st.write(m)

    st.write('Fuentes:  \n https://msi.nga.mil/Piracy  \n https://eng.uber.com/h3/  \n https://spatialthoughts.com/2020/07/01/point-in-polygon-h3-geopandas/')
    
    
	
	


#%%
