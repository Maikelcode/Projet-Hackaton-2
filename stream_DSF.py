import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")   ### Configuration de taille affichage dans la page 

st.title('PROJET HACKATON AVEC LE PARTENAIRE ENTENDS MOI ')

st.image("https://www.entendsmoi.fr/wp-content/uploads/2022/05/Logo-Entends-moi-couleur.png",width=400)


entendsmoi_df = pd.read_csv("https://raw.githubusercontent.com/Maikelcode/Projet-Hackaton-2/46caf904c2626972560a2d3d20002d13d67e36a6/new_top_topics_v2.csv")

# Liste des region :

region = entendsmoi_df["region"].unique()

### Multiselec du choix de la region :
etablissements_selected = st.multiselect("Choix de la region :", region, default = region)

# Selection de ou des regions voulu:

mask_region = entendsmoi_df["region"].isin(etablissements_selected)
entendsmoi_df = entendsmoi_df[mask_region]

### Positif or Negatif
positif_or_not = entendsmoi_df["review_type"].unique() ### Selection avis positif_or_not


positif_selected = st.multiselect("Avis :", positif_or_not, default = positif_or_not)

# Selection de la df selon la selection positif or negatif :
mask_positif = entendsmoi_df["review_type"].isin(positif_selected)
entendsmoi_df = entendsmoi_df[mask_positif]

### Name de l'établissement :
name_id = entendsmoi_df["name"].unique()

select_name = st.selectbox("Nom", name_id)

mask_name_id = entendsmoi_df[entendsmoi_df["name"] == select_name]

st.dataframe(mask_name_id[["name", "region", "review_type","1st_topic", "2nd_topic", "3rd_topic"]])


