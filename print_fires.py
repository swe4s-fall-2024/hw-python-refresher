from utils import get_rows_by_column_value


country = "United States of America"
country_column_index = -1  # TODO: update this
file_path = "./Agrofood_co2_emission.csv"
# TODO
# add code to compute the number of fires so that the following print statement prints
# the number of fires in the given country
print(f"There were {get_rows_by_column_value(file_path, country_column_index)} fires in {country}")