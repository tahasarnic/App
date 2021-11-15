#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:20:33 2021

@author: terens
"""

import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed")

# Başlık
st.title("Egenaz'ın Yapay Zekasına Hoşgeldiniz")

# İstek seçtir
secenek = st.radio("Ne isterseniz Egenaz hanım?", options = ['Mimik yapsın', 'Sohbet etsin', 'Sırtımı kaşısın'])

if secenek == 'Mimik yapsın':
    if st.button('Mimik Değiştir 🤗'):
        mimikler = os.listdir("/img")
        mimikler.remove('.DS_Store')
        st.image(str(random.choice(mimikler)))
        
if secenek == "Sohbet etsin":
    if st.button('Konuş 👦'):
        konus = ['Selaaam 🙋🏻', 'Günün nasıl geçti? 💁🏻‍♂️', 'Kaç çocuk mıncırdın bugün? 👶🏻',
                 'Su içmeyi unutma! 💧', 'Bu çocukla görüşmen nasıl geçti? 😉', 'Bence iyi bir çocuğa benziyor 😛',
                 'Turuncu sana çok yakışıyor 🥕']
        st.write(random.choice(konus))
        
if secenek == "Sırtımı kaşısın":
    if st.button('Sırtımı kaşı 🤤'):
        st.image("kasi.png")
        
        
