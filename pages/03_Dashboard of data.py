import streamlit as st
import pandas as pd
import plotly.express as px

# 📌 Titre de l'application
st.title("📊 Dashboard des Annonces - Expat Dakar")

# 📂 Chargement des données nettoyées
uploaded_file = st.file_uploader("📥 Importer le fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 🧹 Vérification et conversion des données
    df["Prix"] = pd.to_numeric(df["Prix"], errors="coerce")  # Convertir prix en numérique
    df.dropna(subset=["Prix"], inplace=True)  # Supprimer les lignes sans prix

    # 📌 Statistiques générales
    st.subheader("📌 Statistiques Générales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre Total d'Annonces", df.shape[0])
    col2.metric("Prix Moyen (F CFA)", f"{df['Prix'].mean():,.0f}")
    col3.metric("Prix Max (F CFA)", f"{df['Prix'].max():,.0f}")

    # 📊 Histogramme des prix
    st.subheader("📈 Distribution des Prix")
    fig1 = px.histogram(df, x="Prix", nbins=50, title="Répartition des Prix", color_discrete_sequence=["#636EFA"])
    st.plotly_chart(fig1)

    # 📍 Répartition par État (Neuf / Occasion)
    st.subheader("📌 Répartition des Articles Neufs vs Occasion")
    fig2 = px.pie(df, names="Etat", title="État des Produits", hole=0.4, color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig2)

    # 📍 Répartition des annonces par localisation
    st.subheader("📍 Répartition des Annonces par Localisation")
    top_villes = df["Adresse"].value_counts().nlargest(10)  # Top 10 villes
    fig3 = px.bar(x=top_villes.index, y=top_villes.values, labels={"x": "Ville", "y": "Nombre d'annonces"}, title="Top 10 des Villes")
    st.plotly_chart(fig3)

    # 🔍 Tableau interactif
    st.subheader("📋 Données des Annonces")
    st.dataframe(df)

    # 📥 Bouton pour télécharger les données nettoyées
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(label="📥 Télécharger les données en CSV", data=csv, file_name="data_nettoyee.csv", mime="text/csv")
