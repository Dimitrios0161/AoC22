import requests
from bs4 import BeautifulSoup

# load data
def read_data(u,sess):
    url = u
    cookies = {'session': sess}
    session = requests.Session()
    session.cookies.update(cookies)
    page = session.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

# converts a set of 'vertically' listed string-integers to a list of integers
def list_of_ints(l) -> list:
    # 1. stripping returns and replacing them with spaces
    # 2. splitting the elements of the list
    # 3. mapping the string integers to a list of integers
    lst_of_ints = list(map(int,(str(l).replace("/n"," ").strip()).split()))
    return lst_of_ints