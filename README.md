# 🐾 PawPalace

**PawPalace** est une application Django de gestion de pension pour animaux combinée à une boutique e-commerce.  
Elle permet aux utilisateurs de réserver une place pour leur compagnon et d’acheter des accessoires ou produits pour animaux.

## 🧩 Fonctionnalités principales prévues

- Réservation en ligne pour pension (planning, disponibilité, confirmation) ❌
- Espace client sécurisé ❌
- Boutique en ligne (produits, panier, commandes) ❌
- Interface d’administration pour la gestion des réservations et du stock ❌

## 🚀 Stack technique

- **Backend** : Django + SQLite (ou PostgreSQL)
- **Gestion des dépendances** : Poetry
- **Frontend** : HTML/CSS + Django Templates (avec Bootstrap prévu)

## ▶️ Lancer le projet

```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
