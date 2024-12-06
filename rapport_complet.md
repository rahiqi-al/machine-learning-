# Rapport Complet: Prédiction des Prix Immobiliers et Classification des Équipements

Ce rapport présente une analyse détaillée de la méthodologie utilisée pour le projet de prédiction des prix immobiliers et de classification des équipements. Nous discutons également des résultats des modèles, des analyses réalisées, des biais potentiels dans les données, et des améliorations possibles.

---

## 1. Introduction

Le but de ce projet est de prédire les prix des biens immobiliers à partir de diverses caractéristiques, telles que le nombre de chambres, la superficie, les équipements, etc. Nous avons également mis en place un modèle de classification pour prédire la présence d'équipements spécifiques (par exemple, un ascenseur) dans les annonces immobilières.

---

## 2. Méthodologie

### 2.1. Chargement et préparation des données

Les données ont été extraites d'une base de données PostgreSQL contenant plusieurs tables : `Annonce`, `Ville`, `Équipement`, et `AnnonceEquipement`. Nous avons utilisé SQLAlchemy pour interroger et charger ces données dans un dataframe Pandas.

Voici un aperçu des étapes réalisées pour la préparation des données :
1. **Extraction des données** : Les données ont été récupérées à partir de la base de données à l'aide de SQLAlchemy.
2. **Fusion des tables** : Les données des différentes tables ont été fusionnées en un seul dataframe pour simplifier l'analyse.
3. **Gestion des valeurs manquantes** : Nous avons exclu les annonces dont le prix était spécifié comme "PRIX NON SPÉCIFIÉ" ou utilisé l'imputation pour remplir les valeurs manquantes pour certaines variables.
4. **Encodage des variables catégorielles** : Nous avons utilisé l'encodage **One-Hot Encoding** pour convertir des variables comme `city_id` en variables numériques.
5. **Création de variables binaires pour les équipements** : Des colonnes binaires ont été créées pour chaque équipement (par exemple, présence d'un ascenseur).

### 2.2. Modélisation

Deux types de modèles ont été développés dans ce projet : 

1. **Modèle de régression** : Un modèle de régression linéaire a été utilisé pour prédire le prix des biens immobiliers en fonction de plusieurs variables indépendantes.
   - Variables indépendantes : Nombre de chambres (`nb_rooms`), nombre de salles de bain (`nb_baths`), superficie (`surface_area`), et `city_id` (après encodage).
   - Variable cible : Prix de l'annonce (`prix`).

   Le modèle de régression linéaire a été formé en utilisant les données d'entraînement et a été évalué sur les données de test. La performance a été mesurée à l'aide de l'**erreur quadratique moyenne (MSE)** et du **coefficient de détermination R²**.

2. **Modèle de classification** : Un modèle de classification a été développé pour prédire la présence ou l'absence d'un équipement spécifique (par exemple, un ascenseur) dans une annonce.
   - La variable cible est une variable binaire : **1** si l'équipement est présent, **0** si l'équipement est absent.
   - Plusieurs algorithmes ont été testés, notamment la **régression logistique**, les **arbres de décision**, les **forêts aléatoires**, et les **machines à vecteurs de support (SVM)**.

   La performance des modèles a été évaluée à l'aide des **métriques de classification** : 
   - Précision
   - Rappel
   - F1-score
   - AUC-ROC

### 2.3. Évaluation des modèles

#### Modèle de régression
- **Erreur quadratique moyenne (MSE)** : 0,5
- **R²** : 0.31, meaning that 31% of the variation in property prices is explained by the model, while the remaining 69% is due to other factors not captured by the model.

#### Modèle de classification
- Le modèle le plus performant était la **forêt aléatoire**, avec un ***précision** était de 0.96, avec un **rappel** de 0.98, indiquant que le modèle est assez précis pour prédire la présence de l'équipement tout en étant raisonnablement sensible.

---

## 3. Analyse des résultats

### 3.1. Modèle de régression
Le modèle de régression linéaire a montré des résultats modérés, avec un R² de 0,31, ce qui indique que 31 % de la variation des prix des biens immobiliers peut être expliquée par les caractéristiques du modèle. Le MSE est de 0,5, ce qui reflète une erreur moyenne relativement faible, mais suggère encore des opportunités d'amélioration du modèle.

### 3.2. Modèle de classification
Le modèle de classification a donné de bons résultats en termes de capacité à prédire la présence d'un équipement. La forêt aléatoire s'est révélée être la méthode la plus performante, mais des modèles plus complexes, comme les réseaux de neurones, pourraient offrir de meilleures performances si les données le permettent.

---

## 4. Biais et Limites des Modèles

### 4.1. Biais dans les données
- **Biais de sélection** : Si les données disponibles ne sont pas représentatives de l'ensemble du marché immobilier, cela peut introduire des biais dans les prédictions. Par exemple, si la majorité des données provient de certaines régions spécifiques, le modèle peut ne pas bien généraliser à d'autres zones.
- **Biais de présentation** : Les annonces peuvent omettre certains équipements, ce qui peut fausser l'évaluation de la présence des équipements dans les modèles de classification.

### 4.2. Limitations des modèles
- Les **modèles linéaires** peuvent être trop simples pour capturer des relations non linéaires complexes dans les données. Par exemple, l'effet de la **surface** sur le **prix** pourrait être non linéaire, ce qui n'est pas bien capturé par une régression linéaire.
- Le **déséquilibre des classes** dans la variable cible (présence/absence d'équipements) peut poser problème pour les modèles de classification, rendant certaines prédictions moins fiables. Nous avons utilisé des techniques de **suréchantillonnage** et de **sous-échantillonnage** pour traiter ce problème.

---

## 5. Conclusion et Perspectives

Ce projet a permis de développer des modèles de régression et de classification performants pour la prédiction des prix immobiliers et la classification des équipements dans les annonces immobilières. Bien que les modèles soient prometteurs, plusieurs améliorations peuvent être apportées :

1. **Amélioration de la qualité des données** : Enrichir les données avec plus de variables, telles que les descriptions textuelles des annonces, pourrait améliorer les performances.
2. **Modèles plus complexes** : L'utilisation de modèles plus complexes, tels que des réseaux de neurones, pourrait améliorer les résultats, notamment pour la classification des équipements.
3. **Analyse de l'impact des régions** : Une analyse approfondie des différences régionales dans les prix immobiliers pourrait offrir des insights supplémentaires.



