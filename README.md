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
   git clone <url_du_repo>
   cd <nom_du_repo>
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
   uvicorn app.main:app --reload
   ```

## TODO
- [ ] Définir les modèles de données
- [ ] Implémenter la récupération des données via l'API CoinCap
- [ ] Créer les endpoints pour la gestion du portefeuille
- [ ] Écrire des tests unitaires
