def get_rows_by_column_value(file_path, column_index=0, column_value=0):
   matching_rows = []
   f = open(file_path, "r")
   for x in f:
        txt = f.readline()
        i_list = txt.split(", ")
        if column_index == column_value:
            matching_rows.append(i_list)
            print(matching_rows)
   return matching_rows