import json
from easycloudapi.generic.datetime.generate_date_dimention import generate_date_dimension


out1 = generate_date_dimension(start_date="2023\\08\\01", end_date="2023\\08\\03")
print(f"out1: {out1}")

out2 = generate_date_dimension(start_date="2023/08/01", end_date="2023/08/03")
print(f"out2: {out2}")

out3 = generate_date_dimension(start_date="2023-08-01", end_date="2023-08-03")
print(f"out3: {out3}")

