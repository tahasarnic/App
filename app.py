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
#st.title("Egenaz'ın Yapay Zekasına Hoşgeldiniz")

# İstek seçtir
#secenek = st.radio("Ne isterseniz Egenaz hanım?", options = ['Mimik yapsın', 'Sohbet etsin', 'Sırtımı kaşısın'])

#if secenek == 'Mimik yapsın':
#    if st.button('Mimik Değiştir 🤗'):
#        mimikler = ["img/1.jpeg", "img/2.png", "img/3.jpeg", "img/4.webp", "img/5.jpeg", "img/6.png", "img/7.jpeg", "img/8.jpeg", "img/9.jpeg", "img/10.jpeg"]
#        st.image(random.choice(mimikler))
        
#if secenek == "Sohbet etsin":
#    if st.button('Konuş 👦'):
#        konus = ['Selaaam 🙋🏻', 'Günün nasıl geçti? 💁🏻‍♂️', 'Kaç çocuk mıncırdın bugün? 👶🏻',
#                 'Su içmeyi unutma! 💧', 'Bu çocukla görüşmen nasıl geçti? 😉', 'Bence iyi bir çocuğa benziyor 😛',
#                 'Turuncu sana çok yakışıyor 🥕']
#        st.write(random.choice(konus))
        
#if secenek == "Sırtımı kaşısın":
#    if st.button('Sırtımı kaşı 🤤'):
#        st.image("kasi.png")

col1, col2, col3 = st.columns([0.2,1,0.2])
with col2:
    st.title('24 Kasım Öğretmenler Günün Kutlu Olsun Egoş')
    st.balloons()
    st.image('img/cocuklar_egos.png')   
    
with st.expander("Peki kim mi bu Egenaz?👩🏻‍🦰"):
    col7, col8, col9 = st.columns([0.6,1,0.2])
    with col8:
        st.title('Öncelikle kendisi...')
        st.image('img/oscar.jpeg', width = 400)
        
with st.expander("Yaa çok merak ettim, biraz daha bahseder misin?😯 (ve Eren'in mektubu başlar)"):
    col4, col5, col6 = st.columns([0.3,1,0.2])
    with col5:
        st.image('img/mektup.png')
        

with st.expander("Egenaz'ın Beyaz Duvarı 🖼🎭"):
    st.image('img/duvar.png')
        
