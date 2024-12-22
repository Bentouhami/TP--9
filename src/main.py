import os
from data_loader import load_data
from age_analysis import analyze_age_groups
from gender_analysis import analyze_gender_distribution
from customer_segments import analyze_customer_segments

def main():
    """
    Fonction principale qui exécute toutes les analyses.
    """
    # Spécifier le chemin vers le fichier CSV
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                            "data", "customer segment.csv")
    
    # Charger les données
    data = load_data(file_path)
    if data is None:
        return
    
    # Afficher les informations de base sur le dataset
    print("\nInformations sur le dataset :")
    print(data.info())
    
    # Exécuter les différentes analyses
    print("\n1. Analyse par âge :")
    analyze_age_groups(data)
    
    print("\n2. Analyse par genre :")
    analyze_gender_distribution(data)
    
    print("\n3. Analyse des segments clients :")
    analyze_customer_segments(data)

if __name__ == "__main__":
    main()
