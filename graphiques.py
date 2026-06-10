import pandas as pd
import plotly.express as px

# Data
df = pd.DataFrame({
    "Produit": ["Produit A", "Produit B", "Produit C"],
    "Ventes": [1750, 1055, 575],
    "Chiffre_Affaires": [17500, 15825, 11500]
})

# Graphique 1 : ventes par produit
fig1 = px.bar(
    df,
    x="Produit",
    y="Ventes",
    title="Ventes par produit"
)
fig1.show()

# Graphique 2 : chiffre d'affaires par produit
fig2 = px.bar(
    df,
    x="Produit",
    y="Chiffre_Affaires",
    title="Chiffre d'affaires par produit"
)
fig2.show()
