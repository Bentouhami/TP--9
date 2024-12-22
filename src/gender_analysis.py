import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_gender_distribution(data: pd.DataFrame) -> None:
    """
    Visualisation de la répartition des genres et des dépenses.
    
    Args:
        data (pd.DataFrame): DataFrame contenant les données
    """
    plt.figure(figsize=(12, 5))
    
    # Premier subplot : Distribution des genres
    plt.subplot(1, 2, 1)
    gender_counts = data['Genre'].value_counts()
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title("Répartition des Genres")
    
    # Deuxième subplot : Dépenses moyennes par genre
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Genre', y='Montant_Total_d_Achat', data=data)
    plt.title("Distribution des Dépenses par Genre")
    plt.ylabel("Montant Total d'Achat")
    
    plt.tight_layout()
    plt.show()
    
    # Afficher les statistiques
    gender_stats = data.groupby('Genre').agg({
        'Montant_Total_d_Achat': ['mean', 'median', 'count']
    })
    print("\nStatistiques par genre :")
    print(gender_stats)
