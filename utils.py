def get_rows_by_column_value(file_path, column_index):
   matching_rows = []
   f = open(file_path, "r")
   for x in f:
        txt = f.readline()
        i_list = txt.split(", ")
        column_value = len(i_list)
        if column_index == column_value:
            matching_rows.append(i_list)
            print(matching_rows)
   return matching_rows