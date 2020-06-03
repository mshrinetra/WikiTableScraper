import os
import pandas



def create_report_dir(dir_base_name):
  """
  Creates a new directory in current working directory

  Parameters:
  dir_base_name (str): name of the directory

  Returns:
  str:Full path of the new directory
  """

  current_dir = os.getcwd()
  report_dir = os.path.join(current_dir,'Reports')
  if not os.path.exists(report_dir):
    try:
      os.mkdir(report_dir)
    except Exception as e:
      print(e)
      return False

  i = 2
  dir_name = dir_base_name
  while os.path.exists(os.path.join(report_dir, dir_name)):
    dir_name = dir_base_name + "(" + str(i) + ")"
    i = i + 1
  
  try:
    os.mkdir(os.path.join(report_dir, dir_name))
  except Exception as e:
    print(e)
    return False
  
  return os.path.join(report_dir, dir_name)


def save_table_to_csv(report_dir, data_table, file_name='Report'):
  """
  Writes a dictionary list to CSV

  Parameters:
  report_dir (str): Path of report directory
  data_table (list): Dictionary list
  file_name (str): Name of the report file without extention

  Returns:
  bool:Status
  """

  report_file = os.path.join(report_dir, (file_name + ".csv"))
  i = 1
  while os.path.exists(report_file):
    report_file = os.path.join(report_dir, (file_name + "_" + str(i) + ".csv"))
    i = i + 1

  data_frame = pandas.DataFrame(data_table)
  csv_content = data_frame.to_csv(index=False, line_terminator='\n')

  try:
    with open(report_file, "w+", encoding="utf-8", newline="") as f:
      f.write(csv_content)
  except Exception as e:
    print(e)
    return False
  
  return True


if __name__ == "__main__":
  print("This module is only for import and not supposed to be called!")