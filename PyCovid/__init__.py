import requests

def get_stat(respublic_name):
    url='https://disease.sh/v3/covid-19/'
    if respublic_name=='world':
      r=requests.get(url+'all')
      return r.json()
    else:
      r=requests.get(url+'countries/'+respublic_name)
      return r.json()
def get_flag(respublic_name):
    url='https://disease.sh/v3/covid-19/'
    if respublic_name=='world':
      return 'https://images.pexels.com/photos/87651/earth-blue-planet-globe-planet-87651.jpeg'
    else:
      r=requests.get(url+'countries/'+respublic_name)
      j = r.json()
      try:
        return j['countryInfo']['flag']
      except KeyError:
        return "Respublic not found"
      