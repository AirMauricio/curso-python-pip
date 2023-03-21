import utils
import read_csv
import charts
import pandas as pd

def run():

  '''  
  data = list(filter(lambda x : x['Continent'] == 'South America', data))

  country = list(map(lambda x: x['Country/Territory'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  #print(percentage)
  '''
  df = pd.read_csv('data.csv') # Lee a travez de la funcion read_csv de la libreria pandas, el documentos .csv
  df = df[df['Continent'] == 'Africa'] #Filtro para  la columna Continent del archivo csv

  country = df['Country/Territory'].values
  percentage = df['World Population Percentage'].values
  charts.generate_pie_chart(country, percentage)

  data = read_csv.read_csv('data.csv')
  country = input('digita un pais: ')
  print(country)
  
  result = utils.population_by_county(data,country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)    

  
if __name__ == '__main__':
  run()