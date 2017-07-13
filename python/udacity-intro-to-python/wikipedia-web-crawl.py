# udacity intro to python: lesson 5
# wikipedia web crawl
# https://classroom.udacity.com/courses/ud1110/l
# written by: jane yang
# last edited: 13 july 2017

# load modules  
import requests # for grabbing html code
from bs4 import BeautifulSoup # for parsing html data
import time # for delaying code 
            # (to not overwhelm the servers and abide by wikipedia.org/robot.txt)
import urllib # for manipulating urls

# define helper functions
def continue_crawl(search_history, target_url):
    """
    For use in a while loop for crawling a website
    
    Arguments:
    - search_history = a list of string urls that have been visited, in order of visit
    - target_url = if this url is visited, stop the loop
    
    Returns either True or False
    """
    # return False if we land on the target site
    if search_history[-1] == target_url:
        print("We landed on the target site!")
        return False
    # return False if the search history exceeds 25 urls
    elif len(search_history) > 25:
        print("We're tired of crawling. Stopping now that we've visited over 25 sites.")
        return False
    # return False if there is a cycle in the search history
    elif search_history[-1] in search_history[:-1]:
        print("Oops, we've fallen into a cycle!")
        return False
    # otherwise, return True
    else:
        return True

def find_first_link(url):
    """
    Given a url, parse it to return the first link in the html code.
    If there are no links, return None.
    """
    # load html data from url
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # isolate the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    # find all of the article elements that are paragraphs (ignore sidebars, callout boxes)
    for element in content_div.find_all('p', recursive = False):
        # initialize a string to hold the article
        first_relative_link = None
        
        # find the first anchor tag that is a direct child of a paragraph.
        # using direct children avoids accidentally returning a citation or help article,
        # etc.(which are nested in other divs)
        if element.find("a", recursive = False):
            first_relative_link = element.find("a", recursive = False).get("href")
            break
        
        if not first_relative_link:
            return
            
    # build the absolute link by appending the broader wikipedia url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_relative_link)
    return first_link


# define both starting and target urls
start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

# initialize article_chain
article_chain = [start_url]

# run web crawl
while continue_crawl(article_chain, target_url): 
    # print each link visited
    print(article_chain[-1])
    # download html of last article in article_chain and find first link in body
    first_link = find_first_link(article_chain[-1])
    # if there are no links in the article, abort the crawl
    if not first_link:
        print("Whoops! There are no links in this article. Aborting crawl.")
        break
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
    
