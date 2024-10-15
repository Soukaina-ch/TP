import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


cities = pd.read_csv("C:/Users/SoukainaCHAHBA/Downloads/cities.csv", )
cities.head()

hw = pd.read_csv("C:/Users/SoukainaCHAHBA/Downloads/hw_200.csv", )
hw.head()


cities.columns = [col.replace('"', '').strip() for col in cities.columns]

print(cities)

cities['Lat_totale']= cities['LatD'] + (cities['LatM']/ 60) + (cities['LatS'] / 3600)
cities['Long_totale'] = cities['LonD'] + (cities['LonM'] / 60) + (cities['LonS'] / 3600)

print(cities)

#Filtrez le DataFrame df_cities pour obtenir uniquement les villes situées dans l'hémisphère Nord
# (NS == 'N').

cities['NS'] = cities['NS'].str.replace(' "N"','N')  # Enlève les guillemets

print(cities)
cities = cities[cities['NS'] == 'N']
print(cities)

popul = pd.read_csv("C:/Users/SoukainaCHAHBA/Downloads/Population_data.csv")
print(popul)

df = pd.merge(popul, cities, on='City', how='left')  # Utilisez 'outer', 'left' ou 'right' selon le besoin
print(df)
#Q5
df_regroupe= df.groupby('City').agg({
    "Population_2020": "first",
    "Growth_rate": "first"
})
df['population_2025'] = (df['Population_2020']*(1 + (df['Growth_rate']/100)))**5
print(df['population_2025'])

#Q6
df = df[df['population_2025']>1000000]
print(df)

#Q7
population_projetee = df.sort_values(by='population_2025', ascending=False)

top_10_villes = population_projetee.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_villes['City'], top_10_villes['population_2025'], color='red')
plt.title('10 Villes avec la Population Projetée la Plus Élevée en 2025')
plt.xlabel('Ville')
plt.ylabel('Population Projetée en 2025')
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique
plt.show()
#Q7

np.random.seed(0)  # Pour la reproductibilité
df['Area'] = np.random.randint(50, 1001, size=len(df))
df['Densité_population'] = df['Population_2020'] / df['Area']
print(df)

#Q_8

ville_grande_pop = df.loc[df['Densité_population'].idxmax()]

ville_petite_pop = df.loc[df['Densité_population'].idxmin()]


print(ville_grande_pop)


print(ville_petite_pop)

#Q_9


villes_densite_elevee = df[df['Densité_population'] > 5000]

# Afficher les résultats
print(villes_densite_elevee)

#Q10
moyenne_population = df['Population_2020'].mean()

# Calculer la médiane de la population
mediane_population = df['Population_2020'].median()

# Afficher les résultats
print(f"Moyenne de la population: {moyenne_population:.2f}")
print(f"Médiane de la population: {mediane_population:.2f}")

#Q11

min_population = df['Population_2020'].min()
max_population = df['Population_2020'].max()
df['Population_normalisée'] = (df['Population_2020'] - min_population) / (max_population - min_population)
print(df['Population_normalisée'])

#Q12

moyenne = np.mean(df['Population_2020'])
ecart_type = np.std(df['Population_2020'])
minimum = np.min(df['Population_2020'])
maximum = np.max(df['Population_2020'])

# Créer un tableau des statistiques descriptives
statistiques = {
    'Moyenne': moyenne,
    'Écart-type': ecart_type,
    'Minimum': minimum,
    'Maximum': maximum
}

# Convertir le dictionnaire en DataFrame pour un affichage propre
statistiques_df = pd.DataFrame(statistiques, index=[0])

# Afficher le tableau des statistiques descriptives
print(statistiques_df)

