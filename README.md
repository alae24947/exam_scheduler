# exam_scheduler
# Plateforme d'Optimisation des Emplois du Temps d'Examens Universitaires

## Contexte du Projet

Ce projet a été développé dans le cadre du cours de Bases de Données pour répondre à la problématique de gestion des emplois du temps d'examens dans une faculté de plus de 13,000 étudiants répartis sur 7 départements et plus de 200 offres de formation.

La génération manuelle des emplois du temps d'examens génère fréquemment des conflits tels que:
- Surcharge des amphithéâtres
- Chevauchements d'horaires pour les étudiants et professeurs
- Mauvaise répartition des surveillances
- Non-respect des contraintes d'équipements

## Objectifs

- Concevoir une base de données relationnelle pour gérer les examens
- Implémenter un algorithme d'optimisation automatique
- Générer des plannings optimaux en moins de 45 secondes
- Développer une interface web fonctionnelle

## Technologies Utilisées

### Backend
- Python 3.10
- MySQL 
- Bibliothèques: psycopg2, pandas

### Frontend
- Streamlit
- CSS personnalisé

### Base de Données
- SQL pour la modélisation des données
- Procédures stockées pour l'optimisation

## Structure du Projet

```
exam_scheduler/
├── backend/
│   ├── __init__.py
│   ├── analytics.py       # Fonctions d'analyse et KPIs
│   ├── auth.py            # Système d'authentification
│   ├── db.py              # Connexion à la base de données
│   └── scheduler.py       # Algorithme de génération d'emplois du temps
├── database/
│   ├── data.sql           # Données de test
│   └── schema.sql         # Schéma de la base de données
├── frontend/
│   └── styles.css         # Styles personnalisés
├── app.py                 # Application principale Streamlit
└── requirements.txt       # Dépendances du projet
```

## Modèle de Données

### Tables Principales

- **departements**: Gestion des départements de la faculté
- **formations**: Programmes d'études offerts
- **etudiants**: Informations sur les étudiants inscrits
- **modules**: Cours et modules d'enseignement
- **professeurs**: Corps enseignant
- **salles**: Salles et amphithéâtres disponibles
- **examens**: Planning des examens générés
- **inscriptions**: Inscriptions des étudiants aux modules

## Contraintes Implémentées

### Contraintes Étudiants
- Maximum 1 examen par jour par étudiant
- Respect des inscriptions aux modules

### Contraintes Professeurs
- Maximum 3 surveillances par jour
- Équilibrage du nombre de surveillances entre professeurs
- Priorité aux examens du département d'affectation

### Contraintes Salles
- Respect de la capacité maximale
- Salles limitées à 20 étudiants en période d'examen
- Disponibilité des équipements requis

## Installation
### Étapes d'Installation

1. Cloner le repository
```bash
git clone [URL_DU_REPOSITORY]
cd exam_scheduler
```

2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer la base de données
```bash
# Créer la base de données
createdb exam_management

# Exécuter les scripts SQL
psql -d exam_management -f database/schema.sql
psql -d exam_management -f database/data.sql
```

5. Configurer les variables d'environnement
```bash
# Créer un fichier .env sur anaconda 3
DB_HOST=localhost
DB_PORT=5432
DB_NAME=exam_scheduler
DB_USER=root
```

## Utilisation

### Lancer l'Application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse: http://localhost:8501

### Comptes de Test

#### Administrateur
- Username: admin
- Password: admin123

#### Chef de Département
- Username: chef_dept
- Password: dept123

#### Vice-Doyen
- Username: vice_doyen
- Password: doyen123

## Fonctionnalités par Rôle

### Administrateur
- Génération automatique des emplois du temps
- Détection et résolution des conflits
- Gestion complète des ressources
- Accès à tous les tableaux de bord

### Chef de Département
- Consultation du planning de son département
- Validation des plannings
- Statistiques départementales
- Détection de conflits

### Vice-Doyen / Doyen
- Vue stratégique globale
- KPIs académiques
- Taux d'utilisation des ressources
- Statistiques inter-départements

## Tableaux de Bord

### Planning des Examens
Affichage du calendrier complet des examens avec:
- Module
- Date et heure
- Salle assignée
- Filtrage par département/formation

### Statistiques Globales
KPIs principaux:
- Nombre total d'examens
- Taux d'occupation des salles
- Nombre de conflits détectés
- Heures de surveillance par professeur

### Détection des Conflits
- Conflits d'horaires pour les professeurs
- Conflits d'horaires pour les étudiants
- Conflits de capacité des salles
- Alertes en temps réel

## Algorithme d'Optimisation

L'algorithme de génération utilise:
1. Analyse des contraintes par priorité
2. Attribution des créneaux horaires par algorithme glouton
3. Vérification et résolution des conflits
4. Optimisation de l'utilisation des salles
5. Équilibrage des charges de surveillance

