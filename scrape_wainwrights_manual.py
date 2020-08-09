import wikipedia, re
from bs4 import BeautifulSoup

def get_wainwright_coordinates():
    "Get the 8 figure map coordinates for all 214 Wainwrights"
    # Defining a few wikipedia module strings
    wiki_search_string = "list of wainwrights"
    wiki_page_title = "List of Wainwrights"
    wiki_table_caption = "Wainwrights, ranked by height"
    parsed_table_data = []

    search_results = wikipedia.search(wiki_search_string)
    for result in search_results:
        if wiki_page_title in result:
            my_page = wikipedia.page(result)

            # Getting the HTML source
            soup = BeautifulSoup(my_page.html())

            # Matching the caption of our table using a regular expression
            table = soup.find('caption',text = re.compile(r'%s'%wiki_table_caption)).findParent('table')
            rows = table.findAll('tr')

            # Parsing the table data
            for row in rows:
                children = row.findChildren(recursive = False)
                row_text = []
                for child in children:
                    clean_text = child.text
                    # Discarding reference/citation links
                    clean_text = clean_text.split('&91;')[0]
                    # Cleaning header row of sort icons
                    clean_text = clean_text.split('&#160;')[-1]
                    clean_text = clean_text.strip()
                    row_text.append(clean_text)
                parsed_table_data.append(row_text)

    return parsed_table_data

# Main body of the script #
if __name__=="__main__":
    print ('The Wainwright data:\n\n')
    wainwright_data = get_wainwright_coordinates()
    for row in wainwright_data:
        print ('|'.join(row))