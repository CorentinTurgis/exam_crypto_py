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
   source venv/bin/activate
   venv\Scripts\activate
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
[C] Une route /wallet/wealth -> List[{'crypto' : 'btc', 'qtt' : '0.001', 'valeur' : '94_000'}]
[C] Une route POST /wallet/add_one(crypto_name, qtt) -> Ok
[C] Une route POST /wallet/remove_one(crypto_name, qtt) -> Ok

-> api/route/user_router.py
[C] Une route POST /users/register
[C] Une route POST /users/login(user) -> 'user.name_secret'
[C] Une route POST /users/delete

-> core/schemas
[C] wallets_schema.py
[C] users_schema.py
[C] cryptos_schema.py

//Typage
[J] models/wallet_models.py
[J] models/users_models.py
[J] models/crypto_models.py
-- Finalement Wallet pour la vision globale et userAssets pour la liste détaillé ... Evite de forcer une mise à jour à chaque fois

services/auth_service.py
[J] Genere un code secret
[J] Decode un code secret

services/wallet_services.py
[J] Recupere la data brute sur l'api et la transforme pour retourner juste ce qu'il faut
[J] Gere l'ajout d'une crypto dans le wallet
[J] Gere le remove d'une qtt d'une crypto dans un wallet

services/user_service.py
[J] CrudUser

- Proteger les autres routes si le header Bearer != 'code_secret'
