import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_customer_segments(data: pd.DataFrame) -> None:
    """
    Analyse des segments de clients basée sur plusieurs critères.
    
    Args:
        data (pd.DataFrame): DataFrame contenant les données
    """
    plt.figure(figsize=(15, 10))
    
    # Analyse des dépenses par type d'abonnement
    plt.subplot(2, 2, 1)
    sns.boxplot(x='Abonnement', y='Montant_Total_d_Achat', data=data)
    plt.title("Dépenses par Type d'Abonnement")
    plt.xticks(rotation=45)
    
    # Analyse des catégories de produits
    plt.subplot(2, 2, 2)
    category_counts = data['Categories_Produit'].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.title("Répartition des Catégories de Produits")
    
    # Analyse par localisation
    plt.subplot(2, 2, 3)
    sns.boxplot(x='Localisation', y='Montant_Total_d_Achat', data=data)
    plt.title("Dépenses par Localisation")
    plt.xticks(rotation=45)
    
    # Nombre d'achats mensuel moyen par type d'abonnement
    plt.subplot(2, 2, 4)
    sns.barplot(x='Abonnement', y='Nombre_Achat_Mensuel', data=data)
    plt.title("Nombre d'Achats Mensuel Moyen par Abonnement")
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Afficher les statistiques détaillées
    print("\nStatistiques par type d'abonnement :")
    subscription_stats = data.groupby('Abonnement').agg({
        'Montant_Total_d_Achat': ['mean', 'median', 'count'],
        'Nombre_Achat_Mensuel': 'mean'
    })
    print(subscription_stats)
    
    print("\nStatistiques par catégorie de produit :")
    category_stats = data.groupby('Categories_Produit').agg({
        'Montant_Total_d_Achat': ['mean', 'median', 'count']
    })
    print(category_stats)
