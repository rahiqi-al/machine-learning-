
# Prédiction des Prix Immobiliers et Classification des Équipements

Ce projet utilise des modèles d'apprentissage automatique pour :

1. Prédire les prix des biens immobiliers à partir de diverses caractéristiques (nombre de chambres, équipements, etc.).
2. Classer la présence d'équipements spécifiques dans les annonces (par exemple, la présence ou l'absence d'un ascenseur).

---

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :

- **Python** 3.12.3
- **PostgreSQL** (avec les tables nécessaires configurées)
- **Bibliothèques Python** : Les bibliothèques nécessaires sont listées dans le fichier `requirements.txt`.

---

## Installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/rahiqi-al/machine-learning-.git
   ```

2. **Accédez au répertoire du projet** :

   ```bash
   cd machine-learning
   ```

3. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez la base de données** :

   - Modifiez le fichier `config.py` pour inclure vos identifiants PostgreSQL et le nom de la base de données.
   - Assurez-vous que votre base de données PostgreSQL contient les tables suivantes : `Annonce`, `Ville`, `Équipement`, et `AnnonceEquipement`.

---

## Utilisation

1. **Charger les données** :

   - Connectez-vous à la base de données PostgreSQL et importez les données nécessaires des tables.

2. **Prétraitement des données** :

   - Gérer les valeurs manquantes (par exemple, exclure les annonces avec des prix "PRIX NON SPÉCIFIÉ").
   - Encoder les variables catégorielles 
   - Créer des variables binaires pour les équipements (ex. présence d'ascenseur).

3. **Entraînement des modèles** :

   - **Régression linéaire** pour prédire les prix des biens immobiliers.
   - **Classification** (régression logistique, forêt aléatoire, SVM) pour prédire la présence d'équipements spécifiques.

4. **Évaluation des modèles** :

   - **Régression** : Mesurer la performance avec l'Erreur Quadratique Moyenne (MSE) et le R².
   - **Classification** : Évaluer la précision, le rappel, la F1-Score et l'AUC-ROC.

---


## Auteur

Créé par **ALI RAHIQI**. Pour toute question, veuillez contacter [ali123rahiqi@gmail.com](mailto:votre.email@example.com).