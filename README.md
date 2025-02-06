# Gestion de Portefeuille Crypto

## Description
Ce projet consiste en un backend permettant de gérer un portefeuille de cryptomonnaies. Il permet aux utilisateurs de renseigner les cryptos qu'ils possèdent ainsi que leur quantité, puis de calculer leur valeur actuelle en fonction des cours récupérés depuis l'API [CoinCap](https://docs.coincap.io/).

## Stack Technique
- **Langage** : Python
- **Framework** : FastAPI
- **ORM** : Peewee
- **Base de données** : SQLite

## Fonctionnalités
- **Stockage des données des utilisateurs** (crypto et quantité détenue)
- **Récupération des cours des cryptos via API**
- **Calcul de la valeur du portefeuille en temps réel**
- **Endpoints RESTful** pour créer, lire, modifier et supprimer des données

## Architecture
Le projet suit l'architecture recommandée par FastAPI pour les applications de grande taille :
- **/app/** : Dossier principal contenant le code
    - **/api/** : Contient les endpoints
    - **/models/** : Définit les modèles de données (Peewee ORM)
    - **/services/** : Contient la logique métier
    - **/core/** : Configuration de l'application

## Installation
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/CorentinTurgis/exam_crypto_py.git
   cd exam_crypto_py
   ```
2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate  # Sur Windows
   ```
3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
4. **Lancer le serveur FastAPI** :
   ```bash
   fastapi dev app/main.py
   ```

## TODO
###v1
-> api/route/wallet_router.py
[ ] Une route /wallet/wealth -> List[{'crypto' : 'btc', 'qtt' : '0.001', 'valeur' : '94_000'}]
[ ] Une route POST /wallet/add_one(crypto_name, qtt) -> Ok
[ ] Une route POST /wallet/remove_one(crypto_name, qtt) -> Ok

-> api/route/user_router.py
[ ] Une route POST /users/register
[ ] Une route POST /users/login(user) -> 'user.name_secret'
[ ] Une route POST /users/delete

//Typage
[ ] models/wallet_models.py
[ ] models/users_models.py
[ ] models/crypto_models.py

services/auth_service.py
[ ] Genere un code secret
[ ] Decode un code secret

services/wallet_services.py
[ ] Recupere la data brute sur l'api et la transforme pour retourner juste ce qu'il faut
[ ] Gere l'ajout d'une crypto dans le wallet
[ ] Gere le remove d'une qtt d'une crypto dans un wallet

services/user_service.py
[ ] CrudUser

- Proteger les autres routes si le header Bearer != 'code_secret'
