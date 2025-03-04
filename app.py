import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load('./best_model.pkl')

# Récupérer les colonnes attendues par le modèle
expected_columns = model.feature_names_in_

# Titre de l'application
st.title('Prédiction des prix des maisons 🏠')

st.markdown('**Remplissez les caractéristiques suivantes pour prédire le prix :**')

# Création des champs pour chaque feature (adapte selon tes données)
overall_qual = st.number_input('Qualité générale (OverallQual)', min_value=1, max_value=10, value=5)
gr_liv_area = st.number_input('Surface habitable au-dessus du sol (GrLivArea)', min_value=0, value=1500)
garage_cars = st.number_input('Nombre de voitures dans le garage (GarageCars)', min_value=0, value=2)
total_bsmt_sf = st.number_input('Surface totale du sous-sol (TotalBsmtSF)', min_value=0, value=1000)

# Construire le DataFrame pour les prédictions
input_data = pd.DataFrame({
    'OverallQual': [overall_qual],
    'GrLivArea': [gr_liv_area],
    'GarageCars': [garage_cars],
    'TotalBsmtSF': [total_bsmt_sf]
})

# Adapter les colonnes aux attentes du modèle
input_data = input_data.reindex(columns=expected_columns, fill_value=0)

# Afficher les données utilisateur pour vérification
st.subheader('Données saisies :')
st.dataframe(input_data)

# Bouton pour faire la prédiction
if st.button('Prédire le Prix'):
    try:
        prediction = model.predict(input_data)
        st.subheader('Prix Prévu :')
        st.success(f'{prediction[0]:,.2f} $')
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")

# Afficher les colonnes attendues (debugging)
st.sidebar.title('Debugging 🛠️')
st.sidebar.write('Colonnes attendues par le modèle :', expected_columns)
