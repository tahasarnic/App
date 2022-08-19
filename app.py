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
st.title("Egenaz'ın Yapay Zekasına Hoşgeldiniz Vol 2")

st.markdown("Hadi seninle bir güven testi yapalım. Bu aplikasyonun sonuna gelene kadar **SOL** tarafa bakmak yok. Ne zaman **'Şimdi SOL tarafa bakabilirsin'** ifadesiyle karşılaşırsan işte o zaman sol tarafa bakabilirsin. Bu testten geçeceğine %100 eminim.")

sola_bakmak = st.radio('Sola bakmama kararı veriniz:', options = ['Söz söz valla bakmayacağım 😇', 'Bir gözüm kayabilir 😈'], index = 1)
if sola_bakmak == 'Bir gözüm kayabilir 😈':
    st.image('img/ordek.jpeg')
else:
    st.balloons()
    st.image('img/tebrik.png')

st.markdown('Belki bu aplikasyona bakarken seni bana, muhtemelen beni de sana hatırlatan şarkımızı dinlemek istersin 👇')

if st.button('Şarkı Çalsın 🎶'):
    st.video('music/Kaan Boşnak - Seni Buldum Ya.mp4', format='video/mp4')


st.markdown('Evet bu hikayenin konusu da aslında **"seni buldum ya başka ne isterim?"** Gel beraber bu hikayeye bir göz atalım 👀')

st.markdown('## Bizim Kumarımız Burada Biter')

col1, col2 = st.columns([0.3, 1])

with col1:
    hikaye = st.radio('Hikaye seçiniz:', ['Toz Bulutu', 'Haller', 'Kapılar', 'Kazandibi', 'Pokemon', 'Mor', 'Premses', 'NASA', 'Denge', 'Güneş'])
    hikaye_dict = {'Toz Bulutu':'1',
                   'Haller':'2',
                   'Kapılar':'3',
                   'Kazandibi':'4',
                   'Pokemon':'5',
                   'Mor':'6',
                   'Premses':'7',
                   'NASA':'8',
                   'Denge':'9',
                   'Güneş':'10'}

with col2:
    st.image('img1/'+hikaye_dict[hikaye]+'.png')

st.markdown('## Sola Bakmak?')
st.markdown('Tebrikler Ege Naz Bozovalı testi geçtin artık **SOLA BAKABİLİRSİN** 👇')
st.image('img1/20220820_004117.jpg')

cevap = st.radio('Cevabınız?', ['Eveeeeeeeet', 'Nau Nau'])

if cevap == 'Eveeeeeeeet':
    st.image('img1/11.png')
else:
    st.image('img1/12.png')


    


    





















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


