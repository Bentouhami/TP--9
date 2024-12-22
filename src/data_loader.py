import pandas as pd
import os
from typing import Optional

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Charger les données depuis un fichier CSV et nettoyer les colonnes.
    
    Args:
        file_path (str): Chemin vers le fichier CSV
        
    Returns:
        pd.DataFrame: DataFrame nettoyé ou None si une erreur survient
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas")
            
        data = pd.read_csv(file_path, encoding='utf-8', sep=';')
        
        # Renommer les colonnes pour éviter les problèmes d'encodage
        data.rename(columns={
            "Montant Total d'Achat (U)": "Montant_Total_d_Achat",
            "Nombre Achat (par mois)": "Nombre_Achat_Mensuel",
            "Inscription (Annees)": "Annees_Inscription",
            "Categories Produit": "Categories_Produit"
        }, inplace=True)
        
        # Vérifier les données manquantes
        missing_data = data.isnull().sum()
        if missing_data.any():
            print("Attention : Données manquantes détectées :")
            print(missing_data[missing_data > 0])
            
        return data
        
    except Exception as e:
        print(f"Erreur lors du chargement des données : {str(e)}")
        return None
