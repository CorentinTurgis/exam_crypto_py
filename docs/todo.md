# 📌 TODO - Gestion de Portefeuille Crypto

## 📂 Modélisation de la Base de Données
(app.core.schemas.xxx.py)
- [ ] **Créer les modèles suivants** :
    - [ ] `User` : Identifiant unique et nom d'utilisateur *(c)*
    - [ ] `Wallet` : Portefeuille lié à un utilisateur *(c)*
    - [ ] `WalletAsset` : Stockage des cryptos et quantités *(c)*
    - [ ] `CryptoPrice` : Cache des prix en USD *(c)*

## ⚙️ Intégration de l’API CoinCap
- [ ] **Récupérer le prix des cryptos en temps réel** *(j)*
- [ ] **Créer une fonction pour mettre à jour les prix stockés** *(j)*
- [ ] **Optimiser la fréquence des requêtes pour éviter une surcharge** *(j)*

## 🔗 Endpoints RESTful
- [ ] **Créer les endpoints suivants :**
    - [ ] `/wallets` : Créer et récupérer un portefeuille *(c)*
    - [ ] `/wallets/{id}/assets` : Ajouter et gérer des cryptos *(j)*
    - [ ] `/wallets/{id}/value` : Calculer la valeur du portefeuille *(c)*
    - [ ] `/crypto-prices/{symbol}` : Obtenir le prix d’une crypto *(j)*

## 🛠️ Optimisations
- [ ] **Mettre en place un système de cache pour les prix des cryptos** *(j)*
- [ ] **Gérer les erreurs d’API et les exceptions** *(c)*
- [ ] **Ajouter des tests unitaires pour chaque fonction clé** *(j)*

## 🚀 Déploiement
- [ ] **Configurer la base de données SQLite en production** *(c)*
- [ ] **Utiliser Docker pour packager l’application** *(j)*
- [ ] **Déployer l’API sur un serveur (ex: Heroku, AWS, etc.)** *(j)*