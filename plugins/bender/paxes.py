from dateutil.parser import parse

PAXES = [
  {
    'type': 'aus',
    'name': 'PAX Australia',
    'date': parse('2017-10-27 08:00:00 +11:00'),
    'estimated': False
  },
  {
    'type': 'prime',
    'name': 'PAX West',
    'date': parse('2018-08-31 08:00:00 -08:00'),
    'estimated': True
  },
  {
    'type': 'west',
    'name': 'PAX West',
    'date': parse('2018-08-31 08:00:00 -08:00'),
    'estimated': True
  },
  {
    'type': 'south',
    'name': 'PAX South',
    'date': parse('2018-01-12 08:00:00 -06:00'),
    'estimated': False
  },
  {
    'type': 'east',
    'name': 'PAX East',
    'date': parse('2018-04-05 08:00:00 -05:00'),
    'estimated':False
  },
  {
    'type': 'unplugged',
    'name': 'PAX Unplugged',
    'date': parse('2017-11-17 08:00:00 -05:00'),
    'estimated': False
  }
]
