# Discord Embed Bot

## 📖 Description

Ce bot Discord permet de créer des **embeds personnalisés** via une commande slash.

Il utilise un système de permissions basé sur un rôle défini dans le fichier `data.json`.

---

# 🚀 Installation

## 1. Créer un environnement virtuel

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

## 1. Ajouter le token du bot

Créer un fichier `.env` à la racine du projet :

```env
TOKEN=ton_token_ici
```

## 2. Définir le rôle autorisé

Dans `data.json`, mettre l'ID du rôle pouvant utiliser la commande `/add-embed` :

```json
{
    "embedPermission": "1486107299834630255"
}
```

---

# 📂 Structure du projet

```text
project/
│
├── components/
│   └── embed.py          # Commande /add-embed
│
├── data.json             # Rôle autorisé
├── main.py               # Fichier principal
├── .env                  # Token du bot (à ne jamais partager)
├── requirements.txt      # Dépendances
└── README.md
```

---

# ▶️ Utilisation

## Lancer le bot

```bash
python main.py
```

ou

```bash
py main.py
```

## Utiliser la commande

```text
/add-embed channel title description color footer
```

### Exemple

```text
/add-embed #annonces "Titre" "Description" "#ff0000" "Footer"
```

---

# 🔒 Permissions

Seuls les utilisateurs possédant le rôle dont l'ID est défini dans `data.json` peuvent utiliser la commande `/add-embed`.

---

# 📄 Licence

Ce projet est libre d'utilisation et peut être modifié selon vos besoins.
