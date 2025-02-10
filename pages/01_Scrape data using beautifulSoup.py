import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Définition des URLs des catégories
categories = {
    "Réfrigérateurs & Congélateurs": "https://www.expat-dakar.com/refrigerateurs-congelateurs",
    "Climatisation": "https://www.expat-dakar.com/climatisation",
    "Cuisinières & Fours": "https://www.expat-dakar.com/cuisinieres-fours",
    "Machines à Laver": "https://www.expat-dakar.com/machines-a-laver"
}

# Nombre maximal de pages à scraper par catégorie (1 à 50 pages)
pages_par_categorie = {
    "Réfrigérateurs & Congélateurs": list(range(1,221)),
    "Climatisation": list(range(1,126)),
    "Cuisinières & Fours": list(range(1, 101)),
    "Machines à Laver": list(range(1,71))
}

# Fonction de scraping
def scrape_data(base_url, num_pages):
    data = []
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"  # Construction de l'URL de la page
        response = requests.get(url)
        
        if response.status_code != 200:
            st.error(f"Erreur lors de la récupération de la page {page}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        conteneurs = soup.find_all("article", class_="listing-card")

        for conteneur in conteneurs:
            try:
                details = conteneur.find('div', {'class': 'listing-card__header__title'}).text.strip()
                etat = conteneur.find('span', {'class': 'listing-card__header__tags__item listing-card__header__tags__item--condition listing-card__header__tags__item--condition_new'}).text
                adresse = conteneur.find('div', {'class': 'listing-card__header__location'}).text.strip().replace(',\n', '').strip()
                prix = conteneur.find('span', {'class': 'listing-card__price__value 1'}).text.strip().replace('\u202f', '').replace(' F Cfa', '')
                image_lien = soup.find('img', {'class': 'listing-card__image__resource vh-img'})['src']
                data.append({
                    "Details": details,
                    "Etat": etat,
                    "Adresse": adresse,
                    "Prix": prix,
                    "Image": image_lien,
                })
            except AttributeError:
                continue
    
    return pd.DataFrame(data)

# Interface Streamlit
st.title("🌐 Scraper sur Expat-Dakar")
st.write("Sélectionnez la catégorie et le nombre de pages à scraper.")

# Sélection de la catégorie
categorie = st.selectbox("Choisissez une catégorie :", list(categories.keys()))

# Sélection des pages disponibles en fonction de la catégorie
pages_disponibles = pages_par_categorie[categorie]

# Liste déroulante pour le nombre de pages à scraper
num_pages = st.selectbox("Sélectionnez le nombre de pages à scraper :", pages_disponibles)

# Bouton pour lancer le scraping
if st.button("Lancer le Scraping"):
    with st.spinner("Scraping en cours... ⏳"):
        df = scrape_data(categories[categorie], num_pages)
    
    if not df.empty:
        st.success(f"✅ {len(df)} annonces récupérées avec succès !")
        st.dataframe(df)  # Affichage du tableau interactif
        
        # Bouton pour télécharger les données en CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(label="📥 Télécharger les données en CSV", data=csv, file_name="annonces_expat_dakar.csv", mime="text/csv")
    else:
        st.warning("⚠️ Aucune annonce trouvée. Essayez avec plus de pages !")