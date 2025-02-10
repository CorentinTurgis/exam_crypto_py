# 📌 TODO - Gestion de Portefeuille Crypto

## 📂 Modélisation de la Base de Données
(app.core.db)
- [ ] **Créer les modèles suivants** :
    - [x] `Users` : Identifiant unique et nom d'utilisateur
    - [x] `Wallets` : Portefeuille lié à un utilisateur
    - [x] `Cryptos` : Stockage des cryptos et quantités dans un wallet
    - [x] `Assets` : Cache des données de coincap

## ⚙️ Intégration de l’API CoinCap
- [x] **Récupérer le prix des cryptos au moment du /wallet/detail**
- [x] **Créer une fonction pour mettre à jour les prix stockés**
- [ ] **Optimiser la fréquence des requêtes pour éviter une surcharge** *()*

## 🔗 Endpoints RESTful
- [ ] **Créer les endpoints suivants :**
    - [x] `/wallet/create` : Créer et récupérer un portefeuille *()*
    - [x] `/wallet/add` : Ajouter et gérer un wallet *()*
    - [x] `/wallet/detail` : Detail des cryptos dans le wallet *()*
    - [x] `/auth/register` : Enregistre un nouvel utilisateur
    - [x] `/auth/login` : Envoie un token de connexion

## 🛠️ Optimisations
- [ ] **Mettre en place un système de cache pour les prix des cryptos** *()*
- [ ] **Gérer les erreurs d’API et les exceptions** *()*
- [ ] **Ajouter des tests unitaires pour chaque fonction clé** *()*

## 🚀 Déploiement
- [ ] **Configurer la base de données SQLite en production** *()*
- [ ] **Utiliser Docker pour packager l’application** *()*
- [ ] **Déployer l’API sur un serveur (ex: Heroku, AWS, etc.)** *()*