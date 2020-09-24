import pandas as pd
import xlrd

#開檔處理
xlsx_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx"
gapminder = pd.read_excel(xlsx_file)

#print("gapmonder type: ", type(gapminder))
year2002 = gapminder.loc[gapminder['year'] == 2002]
#print(year2002, type(year2002))
table = year2002.sort_values('continent')
#continentSort = gapminder.sort_values('continent')
#print(continentSort)
#table = continentSort.loc[gapminder['year'] == 2002]
#print(table)

table_africa = table[table['continent'] == 'Africa']
table_americas = table[table['continent'] == 'Americas']
table_asia = table[table['continent'] == 'Asia']
table_europe = table[table['continent'] == 'Europe']
table_oceania = table[table['continent'] == 'Oceania']
print("%-10s" %"continent", "%-10s" %"pop", "%-10s" %"lifeExp", "%-10s" %"gdpPercap")

print("%-10s" %"Africa", "%-10d" %table_africa['pop'].sum(), "%-10.3f" %table_africa['lifeExp'].mean(), "%-10.3f" %table_africa['gdpPercap'].mean())

print("%-10s" %"Americas", "%-10d" %table_americas['pop'].sum(), "%-10.3f" %table_americas['lifeExp'].mean(), "%-10.3f" %table_americas['gdpPercap'].mean())

print("%-10s" %"Asia", "%-10d" %table_asia['pop'].sum(), "%-10.3f" %table_asia['lifeExp'].mean(), "%-10.3f" %table_asia['gdpPercap'].mean())

print("%-10s" %"Europe", "%-10d" %table_europe['pop'].sum(), "%-10.3f" %table_europe['lifeExp'].mean(), "%-10.3f" %table_europe['gdpPercap'].mean())

print("%-10s" %"Oceania", "%-10d" %table_oceania['pop'].sum(), "%-10.3f" %table_oceania['lifeExp'].mean(), "%-10.3f" %table_oceania['gdpPercap'].mean())

'''
continent=[]
for col_cont in table['continent']:
#    print("col_cont =", type(col_cont), "\n", col_cont)
    flag = True
    for i in range(len(col_cont)):
        for j in range(len(continent)):
            if col_cont[i] == continent:
                flag = False
                break
    if flag:
        continent.append()
print(continent)
#    if continent != row['continent']
#        continent = row['continent']
        
#for i in range(len(continent)):
    
#    table = year2002[year2002['continent'] == 'Asia']
#    print(table, type(table))
'''
