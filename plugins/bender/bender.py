from datetime import tzinfo, timedelta, datetime
import pytz

from plugins.bender.paxes import PAXES
from plugins.bender.pax import Pax

def next_pax(paxes=None):
  """Return the next Pax"""
  if not paxes:
    paxes = _all_paxes()
  paxes = _sort_paxes(paxes)
  for pax in paxes:
    if pax.date < datetime.utcnow().replace(tzinfo=pytz.utc):
      continue
    return pax

def next_pax_for(paxtype):
  paxes = [pax for pax in _all_paxes() if pax.type == paxtype]
  if len(paxes) > 0:
    return next_pax(paxes=paxes)
  else:
    return []

def _all_paxes():
  return [_dict_to_pax(pax) for pax in PAXES]

def _sort_paxes(paxes):
  return sorted(paxes, key=lambda pax: pax.date)

def _dict_to_pax(pax_dict):
  return Pax(name=pax_dict['name'], type=pax_dict['type'],
             date=pax_dict['date'], estimated=pax_dict['estimated'])
