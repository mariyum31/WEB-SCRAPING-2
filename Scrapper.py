import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\arifk\Downloads\chromedriver_win32 (1)")
browser.get(START_URL)
time.sleep(10)

planet_data = []

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", 
            "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]

def scrape():
    
 
    for i in range(1, 5):
        while True:
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if current_page_num < i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
                
            else:
                        break
                        
                        
            for ul_tag in soup.find_all("ul", attrs={"class", "Brightest Star"}):
                li_tags = ul_tag.find_all("li")
                temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

                        hyperlink_li_tags = li_tags[0]
                        temp_list.append("https://exoplanets.nasa.gov/"+ hyperlink_li_tags.find_all("a",href = True) [0]["href"])
                        planet_data.append(temp_list)

                        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
                        with open("scrapper_2.csv", "w") as f:
                            csvwriter = csv.writer(f)
                            csvwriter.writerow(headers)
                            csvwriter.writerows(planet_data)
                            scrape()                                



