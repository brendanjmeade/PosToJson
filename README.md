# PosToJson
Convert directory of .pos files to a single .json file

Daily PBO GPS position time series are stored as .pos files and available at: ftp://data-out.unavco.org/pub/products/position

The .json format applies the following pattern:

[
  {
    "name": "000841",
    "start": 985928400,
    "lon": [139.06990407, 139.069904, 139.06990413, ...],
    "lat": [34.949757897, 34.949757882, 34.949757941, ...]
  },{
    "name": "000842",
    "start": 982818000,
    "lon": [...],
    "lat": [...]
  },{
  ...

  {
    "name": "99R004",
    "start": 1364875200,
    "lon": [...],
    "lat": [...]
  },{
    "name": "99R006",
    "start": 1364875200,
    "lon": [...],
    "lat": [...]
  }
]
