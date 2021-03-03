import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += float(decimal.Decimal(step))

def range_float(start, stop, step):
  range_list = []
  while start < stop:
    range_list.append(start)
    start += float(decimal.Decimal(step))
  yield range_list