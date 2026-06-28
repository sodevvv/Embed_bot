Discord Embed Bot - README

Description
Ce bot Discord permet de créer des embeds personnalisés via une commande slash. Il utilise un système de permissions basé sur un rôle défini dans le fichier data.json.

Installation

1. Cloner le projet
python -m venv venv
source venv/bin/activate   (Linux / Mac)
venv\Scripts\activate      (Windows)

2. Installer les dépendances
pip install -r requirements.txt

Configuration

1. Ajouter le token du bot
Créer un fichier .env à la racine du projet contenant :
TOKEN=ton_token_ici

2. Définir le rôle autorisé
Dans data.json, mettre l’ID du rôle qui peut utiliser la commande /add-embed :
{
    "embedPermission": "1486107299834630255"
}

Structure du projet
project/
components/
    embed.py        -> Commande /add-embed
data.json           -> Rôle autorisé
main.py             -> Fichier principal
.env                -> Token du bot (ne pas partager)
requirements.txt    -> Dépendances

Utilisation

1. Lancer le bot
python ou py bot.py

2. Utiliser la commande
/add-embed channel title description color footer

Exemple :
/add-embed #annonces "Titre" "Description" "#ff0000" "Footer"

Permissions
Seuls les utilisateurs possédant le rôle dont l’ID est défini dans data.json peuvent utiliser la commande /add-embed.