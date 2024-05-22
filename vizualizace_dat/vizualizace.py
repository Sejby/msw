import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('car_prices.csv')

print(data.head())

# Ceny prodaných vozidel oproti jejich počtu
def ceny_graf():
    plt.hist(data['sellingprice'], bins=20, color='blue')
    plt.title('Rozložení cen prodaných vozidel')
    plt.xlabel('Cena')
    plt.ylabel('Počet vozidel')
    plt.show()

# Koláčový graf pro zastoupení barev vozidel
def barvy_graf():
    colors = data['color'].value_counts()
    plt.pie(colors, labels=colors.index, autopct='%1.1f%%', startangle=140)
    plt.title('Barvy vozidel')
    plt.show()

# Rok výroby oproti prodejní ceně
def roky_vs_cena_graf():
    plt.scatter(data['year'], data['sellingprice'])
    plt.title('Rok výroby oproti prodejní ceně')
    plt.xlabel('Rok výroby')
    plt.ylabel('Prodejní cena')
    plt.show()

# Průměrná prodejní cena vozidel pro každý rok výroby
def prumerne_ceny_graf():        
    prumerne_ceny = data.groupby('year')['sellingprice'].mean()
    prumerne_ceny.plot(kind='bar', color='skyblue')
    plt.title('Průměrná prodejní cena vozidel pro každý rok výroby')
    plt.xlabel('Rok výroby')
    plt.ylabel('Průměrná prodejní cena')
    plt.show()
    
# Distribuce stavů vozidel
def distribuce_stavu_vozidel():
    data['condition'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Distribuce stavů vozidel')
    plt.xlabel('Stav')
    plt.ylabel('Počet vozidel')
    plt.show()


prumerne_ceny_graf()