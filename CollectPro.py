import streamlit as st

# Configuration de la page principale
st.set_page_config(page_title="Mon Application", layout="wide")

# Menu principal dans la sidebar
st.sidebar.title("🔍 Navigation")
menu = st.sidebar.selectbox("📌 Choisissez une page :", ["Home", "Fonctionnalités"])

# Affichage de la page Home
if menu == "Home":
    st.title("🏠 Accueil de l'application")
    st.write("""
        Bienvenue dans notre application !  
        Cette application vous permet de scraper des données à l'aide de BeautifulSoup, 
        de les télécharger, de visualiser un tableau de bord des données. Egalement un formulaire est disponible afin de recolter les avis des utilisateurs sur cette application
    """)


    st.write("""
       Les données concernent les annonces sur les réfrigérateurs-congélateurs, climatisation,
        cuisinières-fours et machines-à-laver à partir de la page web expat-dakar 
        * **Libraires python:** base64, pandas, requests, bs4, streamlit, seaborn, matplotlib, plotly.express
        * **Source des données:** [Expat-Dakar](https://www.expat-dakar.com/)
    """)


# Affichage de la page Fonctionnalités
elif menu == "Fonctionnalités":
    # Sous-menu des fonctionnalités dans la sidebar
    sous_menu = st.sidebar.radio("📌 Sélectionnez une fonctionnalité :", [
        "Scrape data using BeautifulSoup", 
        "Download scraped data", 
        "Dashboard of data", 
        "Fill the form"
    ])

    if sous_menu == "Scrape data using BeautifulSoup":
        st.switch_page("pages/01_Scrape data using beautifulSoup.py")  # Redirection vers la page de scraping
    elif sous_menu == "Download scraped data":
        st.switch_page("pages/02_Download scraped data.py")  # Redirection vers la page de téléchargement
    elif sous_menu == "Dashboard of data":
        st.switch_page("pages/03_Dashboard of data.py")  # Redirection vers la page de dashboard
    elif sous_menu == "Fill the form":
        st.switch_page("pages/04_Fill the form.py")  # Redirection vers la page de formulaire
