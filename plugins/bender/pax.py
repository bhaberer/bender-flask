
class Pax():
  def __init__(self, type=None, date=None, name=None, estimated=None):
    self.type = type
    self.date = date
    self.name = name
    self.estimated = estimated

  def countdown_text(self):
    return str(self.date)


  def _build_time_hash(secs, units):
      return {'days': (secs / 86_400).floor,
              'hours': int((secs % 86_400) / 3600),
              'mins': int((secs % 3_600)  / 60),
              'seconds': int(secs % 60)}

  def _parse_time_hash(times, format)
    string = []
    times.each_pair do |period, time|
      next unless period == :seconds || !(time.zero? && string.empty?)

      string << [time, format == :long ? " #{period}" : period.slice(0)].join
    end
    string.join(', ')
