import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


lesDonneesDesComptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "administrateur",
        },
    }
}
comptes = pd.read_csv("lesDonneesDesComptes.csv")

data = {"usernames": {}}
for _, row in comptes.iterrows():
    username = row["usernames"]
    # Remove the 'username' field from the inner dictionary
    user_data = row.drop(labels="usernames").to_dict()
    data["usernames"][username] = user_data


authenticator = Authenticate(data, "cooke", "key", 30)

authenticator.login()


def accueil():

    with st.sidebar:
        selection = option_menu(
            menu_title=None, options=["Accueil", "Les photos de mon chat"]
        )

    if selection == "Accueil":
        st.title("Bienvenue sur ma page")
        st.image(
            "https://gifdb.com/images/high/standing-ovation-crowd-applause-oscar-awards-ai72icmh1ac7apdz.gif"
        )
    elif selection == "Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat 🐱")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(
                "https://www.salisbury.sa.gov.au/assets/images/Services/_800x418_crop_center-center_82_none/Services-Pets-Animals-Cats-01.jpg?mtime=1626181965"
            )
        with col2:
            st.image(
                "https://i.natgeofe.com/n/9135ca87-0115-4a22-8caf-d1bdef97a814/75552.jpg"
            )
        with col3:
            st.image(
                "https://mediaproxy.salon.com/width/1200/https://media2.salon.com/2022/05/cats-party-0516221.jpg"
            )


if st.session_state["authentication_status"]:
    accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplies")
