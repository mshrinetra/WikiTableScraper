from bs4 import BeautifulSoup


def get_wiki_tables(source_html):
  """
  Scraps table from raw html

  Parameters:
  source_html (str): html text

  Returns:
  list: List html tables
  """

  soup = BeautifulSoup(source_html, 'lxml')
  tables = soup.find_all('table', class_='wikitable')
  return tables


def clean_text(html_text):
  """
  Get cleaned text

  Parameters:
  html_text (str): Raw html text

  Returns:
  str: Cleaned text
  """

  raw_text = html_text.text

  references = html_text.find_all('sup', class_='reference')
  for reference in references:
    raw_text = raw_text.replace(reference.text,'')
  
  raw_text_ASCII_only = ''.join([x if ord(x) < 128 else '' for x in raw_text])
  raw_text_without_nl = raw_text_ASCII_only.replace('\n', ' ').replace('\r', ' ')
  raw_text = raw_text_without_nl.replace('  ',' ')
  
  return raw_text.strip()


def get_table_name(table_html):
  """
  Get the name of the table if it is their

  Parameters:
  source_html (str): html text

  Returns:
  str: Name of thable
  bool: Status
  """
  try:
    table_caption_raw = table_html.find('caption')
    if table_caption_raw:
      return clean_text(table_caption_raw)
  except Exception as e:
    return False




def scrap_table(table_html):
  """
  Scraps table from raw html

  Parameters:
  source_html (str): html text

  Returns:
  list: List of dictionary
  """

  data_table = []
  data_keys = []

  rows = table_html.find_all('tr')
  headers = rows[0].find_all('th')
  if not headers:
    headers = row[0].find_all('td')

  for header in headers:
    header_text = clean_text(header)
    data_keys.append(header_text)

  i = 1
  while i < len(rows):
    data_row = {}

    cells = rows[i].find_all('td')
    j=0
    while j < len(data_keys):
      try:
        cell_text = clean_text(cells[j])
        data_row[data_keys[j]] = cell_text
      except Exception  as e:
        print(e)
      j=j+1
    
    data_table.append(data_row)
    i = i+1

  return data_table

if __name__ == "__main__":
  print("This module is only for import and not supposed to be called!")