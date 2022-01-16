import pandas as pd
from selenium import webdriver

# driver downloaded in step 3 and unziped in step 4 of setting up Chrome and Chromedriver.
chrome_webdriver_path = "/Users/abderraoufbenchoubane/Documents/medium_articles_repo/medium_articles_code/web_scraping_selenium_pandas/chromedriver"

# replace Chrome with you browser of choice
driver = webdriver.Chrome(chrome_webdriver_path)
driver.get(
    "https://www.python.org/events/python-events/")

# In this particular Web page we can see that we have Upcoming events and Missed events, both these lists have the same CSS clas
upcoming_event_div = driver.find_element_by_class_name("shrubbery")

events_titles = events_titles = [
    title.text for title in upcoming_event_div.find_elements_by_class_name("event-title")]

events_links = [link.get_attribute("href") for link in upcoming_event_div.find_elements_by_css_selector(
    ".event-title a")]
events_dates = [
    date.text for date in upcoming_event_div.find_elements_by_tag_name("time")]
events_locations = [location.text for location in upcoming_event_div.find_elements_by_class_name(
    "event-location")]

scaped_data_dict = {"Dates": events_dates, "Title": events_titles,
                    "Location": events_locations, "Link": events_links}

# creating the data frame
data_frame = pd.DataFrame(scaped_data_dict)

# saving the content of the data frame to a csv file
data_frame.to_csv("upcoming_python_events.csv")

driver.quit()
