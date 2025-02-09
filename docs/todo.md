# 📌 TODO - Gestion de Portefeuille Crypto

## 📂 Modélisation de la Base de Données
(app.core.db)
- [ ] **Créer les modèles suivants** :
    - [x] `User` : Identifiant unique et nom d'utilisateur
    - [x] `Wallet` : Portefeuille lié à un utilisateur *()*
    - [x] `WalletAsset` : Stockage des cryptos et quantités *()*
    - [x] `CryptoPrice` : Cache des prix en USD *()*

## ⚙️ Intégration de l’API CoinCap
- [ ] **Récupérer le prix des cryptos en temps réel** *()*
- [ ] **Créer une fonction pour mettre à jour les prix stockés** *()*
- [ ] **Optimiser la fréquence des requêtes pour éviter une surcharge** *()*

## 🔗 Endpoints RESTful
- [ ] **Créer les endpoints suivants :**
    - [ ] `/wallets/create` : Créer et récupérer un portefeuille *()*
    - [ ] `/wallets/{id}/add` : Ajouter et gérer des cryptos *()*
    - [ ] `/wallets/{id}/value` : Calculer la valeur du portefeuille *()*
    - [ ] `/wallets/{id}/detail` : Detail des cryptos dans le wallet *()*
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