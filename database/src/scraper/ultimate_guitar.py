import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def main():

    print('Hello World!')

    # URL = "https://realpython.github.io/fake-jobs/"
    # page = requests.get(URL)

    # print(page.text)
    # soup = BeautifulSoup(page.content, "html.parser")
    # results = soup.find(id="ResultsContainer")
    # print(results.prettify())
    
    # job_cards = results.find_all("div", class_="card-content")
    # python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())
    # python_jobs
    
    # python_job_cards = [h2_element.parent.parent.parent for h2_element in python_jobs]
    # python_job_cards[0]
    
    # for job_card in python_job_cards:
    #     title_element = job_card.find("h2", class_="title")
    #     company_element = job_card.find("h3", class_="company")
    #     location_element = job_card.find("p", class_="location")
    #     print(title_element.text.strip())
    #     print(company_element.text.strip())
    #     print(location_element.text.strip())
    #     print()
    
    
    # for job_card in python_job_cards:
    #     links = job_card.find_all("a")
    #     for link in links:
    #         link_url = link["href"]
    #         print(f"Apply here: {link_url}\n")
        

    guitar_URL = 'https://tabs.ultimate-guitar.com/tab/coldplay/yellow-chords-114080'
    page2 = requests.get(guitar_URL)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    print(soup2.prettify())
    song_tuning_key_capo = soup2.find('section', class_="Y9v5o")
    

if __name__ == "__main__":
    main()