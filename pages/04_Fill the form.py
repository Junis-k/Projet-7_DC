# intégration de formulaire de remplissage provenant de KoboToolbox

import streamlit as st

# Centrer le titre
st.markdown("<h1 style='text-align: center;'>Votre avis nous intéresse!</h1>", unsafe_allow_html=True)


# URL du formulaire KoboToolbox (remplace avec ton lien)
kobo_url = "https://ee.kobotoolbox.org/single/5ab8b7fd95fdaed3bf86aa6ea9079064"

# Intégration du formulaire avec un iframe
st.components.v1.iframe(kobo_url, width=800, height=2000)
# st.components.v1.html(f'<iframe src="{kobo_url}" width="700" height="800"></iframe>')