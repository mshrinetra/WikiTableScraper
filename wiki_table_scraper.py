import requests
from src.table_scraper import get_wiki_tables, get_table_name, scrap_table
from src.save_to_csv import create_report_dir, save_table_to_csv

def scrap_wiki_table(url_to_scrap):
  """
    Scraps wikipedia table for given url

    Parameters:
    url_to_scrap (str): url of wikipedia page
  """
# url_to_scrap = 'https://en.wikipedia.org/wiki/Demographics_of_the_world'

  report_dir_name = url_to_scrap.split('/')[len(url_to_scrap.split('/')) - 1] 

  response = requests.get(url_to_scrap)
  if response.status_code == 200:
    report_dir = create_report_dir(report_dir_name)
    source_html = response.text
    tables = get_wiki_tables(source_html)
    for table in tables:
      table_name = get_table_name(table)
      data = scrap_table(table)
      if table_name:
        save_table_to_csv(report_dir, data, table_name)
      else:
        save_table_to_csv(report_dir, data)
        
  else:
    print("Failed to get the page.")


if __name__ == '__main__':
  wiki_url = input("Please enter the Wikipedia page URL to scrap: ")
  scrap_wiki_table(wiki_url)

