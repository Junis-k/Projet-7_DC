""" importation des bibliothèques nécessaires """

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Interface Streamlit
st.title("📥 Télécharger les données scrapées sur Expat-Dakar")
st.write("Sélectionnez la catégorie et le nombre de pages à scraper.")

# fonction de chargement des données déja scrapées
def load_data(dataframe, title, key):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    
    if st.button(title,key):
        st.subheader('Données scrapées')
        st.write('Dimensions des données: ' + str(dataframe.shape[0]) + ' lignes et ' + str(dataframe.shape[1]) + ' colonnes.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 4em;
    width: 30em;
}</style>''', unsafe_allow_html=True)

# ajouter des filtres par état, adresse et prix pour les données

st.sidebar.markdown('Filtres')
Etat = st.sidebar.selectbox('Etat', ['Neuf', "D'Occasion" , 'Venant', 'Reconditionné'])
Adresse = st.sidebar.selectbox('Adresse', ['Thiès', 'Mbour', 'Saint-Louis', 'Touba', 'Kaolack', 'Ziguinchor', 'Louga', 'Fatick', 'Diourbel', 'Kolda', 'Tambacounda', 'Matam', 'Kaffrine', 'Kédougou', 'Sédhiou'])
Prix = st.sidebar.slider('Prix', 0, 1000000, (0, 1000000))

# activer les filtres
def filter_data(dataframe, Etat, Adresse, Prix):
    filtered_data = dataframe
    if Etat != 'Tous':
        filtered_data = filtered_data[filtered_data['Etat'] == Etat]
    if Adresse != 'Tous':
        filtered_data = filtered_data[filtered_data['Adresse'] == Adresse]
    filtered_data = filtered_data[(filtered_data['Prix'] >= Prix[0]) & (filtered_data['Prix'] <= Prix[1])]
    return filtered_data

# Charger les données
load_data(pd.read_csv('Beautifoul_Soup_data/base_donnee_url1.csv'), 'Données sur les réfrigérateurs-congelateurs', '1')
load_data(pd.read_csv('Beautifoul_Soup_data/base_donnee_url2.csv'), 'Données sur les climatisations', '2')
load_data(pd.read_csv('Beautifoul_Soup_data/base_donnee_url3.csv'), 'Données sur les cuisinières-fours', '3')
load_data(pd.read_csv('Beautifoul_Soup_data/base_donnee_url4.csv'), 'Données sur les machines-à-laver', '4')
