import matplotlib.pyplot as plt # Se esta utilizando el modulo pyploty se agino un alias "plt"
'''
libreria matplotlib: https://matplotlib.org/
  Para importar esta librería se debe descargar e incorporar al poryecto
'''

def generate_bar_chart(labels, values): 
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) 
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [10003,450,84500]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)