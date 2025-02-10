# 🚀 API de Gestion de Portefeuille Crypto

## 📌 Description
Cette API permet de gérer un portefeuille de cryptomonnaies. Elle fournit des endpoints pour l'authentification, la gestion des utilisateurs, des portefeuilles et des actifs cryptographiques.

---

## 🛠 Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/CorentinTurgis/exam_crypto_py.git
   cd exam_crypto_py
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   # pip install fastapi==0.115.8 \
   # peewee==3.17.9 \
   # pydantic==2.10.6 \
   # PyJWT==2.10.1 \
   # python-dotenv==1.0.1 \
   # pytz==2025.1 \
   ```

4. **Créer un fichier `.env` avec les variables suivantes** :
   ```ini
   SECRET_KEY=your_secret_key
   DATABASE_URL=database_name
   ```

5. **Lancer le serveur FastAPI** :
   ```bash
   fastapi dev app/main.py
   ```

---

## 📌 Endpoints

### 🔑 **Authentification**
- **POST `/auth/login`** : Connexion d'un utilisateur → Retourne un token JWT.
    - **Body JSON :**
      ```json
      {
        "email": "user@example.com",
        "password": "password123"
      }
      ```
- **POST `/auth/register`** : Inscription d'un nouvel utilisateur.
    - **Body JSON :**
      ```json
      {
        "first_name": "John",
        "last_name": "Doe",
        "username": "j.doe",
        "email": "user@example.com",
        "password": "password123"
      }
      ```

### 💰 **Portefeuilles**
- **POST `/wallet/create`** : Créer un portefeuille.
    - **Body JSON :**
      ```json
      {
        "name": "Mon Portefeuille"
      }
      ```
- **POST `/wallet/add`** : Ajoute une crypto.
    - **Body JSON :**
      ```json
      {
        "crypto_id": "bitcoin",
        "amount": 0.5
      }
      ```
- **GET `/wallets/detail`** : Affiche le prix du portefeuille.

---

## 🚀 Déploiement avec Docker(ne fonctionne pas super)

1. **Construire et lancer le conteneur** :
   ```bash
   docker-compose up --build -d
   ```

2. **Vérifier les logs** :
   ```bash
   docker-compose logs -f
   ```

3. **Arrêter les conteneurs** :
   ```bash
   docker-compose down
   ```

---
