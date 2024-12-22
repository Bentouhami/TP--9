# Analyse de Segments Clients

Ce projet analyse les données de segments clients pour identifier des tendances dans les comportements d'achat, les préférences par âge, genre et localisation.

## Structure du Projet
```
pandas_project/
│
├── data/
│   └── customer segment.csv
│
├── src/
│   ├── main.py               # Point d'entrée du programme
│   ├── data_loader.py        # Chargement et nettoyage des données
│   ├── age_analysis.py       # Analyses liées à l'âge
│   ├── gender_analysis.py    # Analyses liées au genre
│   └── customer_segments.py  # Analyses des segments clients
│
├── requirements.txt          # Dépendances du projet
└── README.md                # Ce fichier
```

## Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ou téléchargez ce projet sur votre machine

2. Ouvrez un terminal et naviguez vers le dossier du projet :
```bash
cd chemin/vers/pandas_project
```

3. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
```

4. Activez l'environnement virtuel :
- Windows :
```bash
venv\Scripts\activate
```
- Linux/Mac :
```bash
source venv/bin/activate
```

5. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Assurez-vous que le fichier de données "customer segment.csv" est présent dans le dossier "data"

2. Exécutez le programme :
```bash
python src/main.py
```

Le programme générera plusieurs visualisations et affichera des statistiques sur :
- La répartition des âges et leur impact sur les achats
- La distribution des genres et leurs comportements d'achat
- Les segments clients par type d'abonnement et catégorie de produit

## Résultats

Le programme génère plusieurs graphiques :
- Distribution des dépenses par groupe d'âge
- Répartition des genres et leurs habitudes d'achat
- Analyse des segments clients par type d'abonnement
- Répartition des catégories de produits

Les résultats sont affichés à la fois sous forme de graphiques et de statistiques dans la console.

## Dépannage

Si vous rencontrez des erreurs :
1. Vérifiez que Python 3.8+ est installé : `python --version`
2. Vérifiez que toutes les dépendances sont installées : `pip list`
3. Assurez-vous que le fichier CSV est présent dans le dossier "data"
4. Vérifiez que l'encodage du fichier CSV est en UTF-8

## IDE développement utilisé

- [Windsurf](https://codeium.com/windsurf)

## IA utilisée

- [ChatGPT](https://chat.openai.com/)
- OpenCascade de Windsurf
- [Claude](https://claude.ai/)

## Contact

Pour toute question ou problème, veuillez contacter : Bentouhami Faisal / bentouhami.faisal@gmail.com

## Remerciements

- merci à tous ceux qui ont contribué au projet, notamment :
    - [Windsurf](https://codeium.com/windsurf)
    - [ChatGPT](https://chat.openai.com/)
    - [Claude](https://claude.ai/)
    - Professeur M. Douvain.