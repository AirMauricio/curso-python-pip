import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda x : x['Continent'] == 'South America', data))

  country = list(map(lambda x: x['Country/Territory'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  #print(percentage)
  charts.generate_pie_chart(country, percentage)

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