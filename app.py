import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
df['color_r'] = 0
df['color_g'] = 0
df['color_b'] = 255
df['color'] = '[255,0,0]'

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            # original, works
            # get_color='[200, 30, 0, 160]',

            # GetColorR/G/B, does not work:
            # getColorR=255,
            # getColorG=0,
            # getColorB=0,
            
            # getting colors from columns, does not work:
            # getColorR='[color_r]',
            # getColorG='[color_g]',
            # getColorB='[color_b]',
            
            # getting colors from single column, this is what I actually would like to do, does not work
            # getColor='[color]'

            # or maybe like this? does not work either
            # getColor='[color]'.split(','),

            get_radius=200,
        ),
    ],
))
