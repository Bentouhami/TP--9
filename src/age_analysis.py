import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_age_groups(data: pd.DataFrame) -> pd.Series:
    """
    Analyse de l'âge moyen par segments d'âge.
    
    Args:
        data (pd.DataFrame): DataFrame contenant les données
        
    Returns:
        pd.Series: Âge moyen par groupe d'âge
    """
    bins = [0, 25, 35, 45, 55, 100]
    labels = ['18-25', '26-35', '36-45', '46-55', '55+']
    
    data['Age_Group'] = pd.cut(data['Age'], bins=bins, labels=labels)
    avg_age = data.groupby('Age_Group').agg({
        'Age': 'mean',
        'Montant_Total_d_Achat': 'mean'
    })
    
    print("\nStatistiques par groupe d'âge :")
    print(avg_age)
    
    # Visualisation
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Age_Group', y='Montant_Total_d_Achat', data=data)
    plt.title("Distribution des Dépenses par Groupe d'Âge")
    plt.xticks(rotation=45)
    
    plt.subplot(1, 2, 2)
    age_counts = data['Age_Group'].value_counts()
    plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%')
    plt.title("Répartition des Groupes d'Âge")
    
    plt.tight_layout()
    plt.show()
    
    return avg_age
