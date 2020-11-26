import requests
import sys
import os
import json
# from .funcmodule import my_function
from bs4 import BeautifulSoup

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
if (os.environ.get("CLICOLOR") is None):
    CLICOLOR = True
else:
    CLICOLOR = os.environ.get("CLICOLOR") == "1" or os.environ.get("CLICOLOR") == 1

def main():
    # support colored print statements
    noColor = '\033[0m'
    redColor = '\033[91m'
    greenColor = '\033[92m'
    dgrayColor = '\033[90m'
    purpleColor = '\033[95m'
    args = sys.argv[1:]
    ## support help
    if len(args) < 1:
        print("HenZCLI tool is used for checking healthy links in HTML file")
        print("Basic usage as follow\n")
        print("\thenzcli <path to html file> <another file>\n")
    else:
        ## support link list flag, bad code :(
        onlyGood = onlyBad = None
        allIncluded= True
        if (args[0] == "--good"):
            onlyGood = True
            allIncluded = False
        elif (args[0] == "--bad"):
            onlyBad = True
            allIncluded = False
        elif (args[0] == "--all"):
            allIncluded = True
        if (args[0] == "-v" or args[0] == "--version"):
            print("HenZCLI version 0.1")
        print('passed argument :: {}'.format(args))
        for arg in args:
            if (arg[0] != "-"):
                if (arg == "telescope"):
                    # Get request http://localhost:3000/posts/
                    r = requests.get('http://localhost:3000/posts')
                    # parse result as JSON object
                    jsonTele = r.json()
                    # reading through each url in JSON objects
                    text = ""
                    for link in jsonTele:
                        # GET request to each post 
                        r = requests.get('http://localhost:3000' + link["url"])
                        text += r.json()["html"]
                    # parse/ammend all of them into 1 file
                    f = open("telescope.html", 'a')
                    f.write(text)
                try: 
                    if (arg == "telescope"):
                        f = open("telescope.html", "r")
                    else:
                        f = open(arg, "r")
                    if (CLICOLOR):
                        print(purpleColor +  "In file " + arg + noColor)
                    else:
                        print("In file " + arg)
                    # parse html file
                    html = BeautifulSoup(f, 'html.parser')
                    # look for all link in a tags
                    for link in html.find_all('a'):
                        URL = link.get('href').strip()
                        if (URL.find("http") == 0):
                            try:
                                # test links
                                requestObj = requests.get(URL)
                                if ((onlyBad or allIncluded) and requestObj.status_code == 404 or requestObj.status_code == 401):
                                    if (CLICOLOR):
                                        print(redColor + "Bad link " + URL + noColor)                                    
                                    else:
                                        print("Bad link " + URL)
                                elif ((onlyGood or allIncluded) and requestObj.status_code == 200):
                                    if (CLICOLOR):
                                        print(greenColor + "Good link " + URL + noColor)
                                    else:
                                        print("Good link " + URL)
                                else:
                                    if (allIncluded):
                                        if (CLICOLOR):
                                            print(dgrayColor + "Unknown "+ URL + noColor)
                                        else:
                                            print("Unknown "+ URL)
                            except:
                                if (allIncluded):
                                    if (CLICOLOR):
                                        print(dgrayColor + "Unknown "+ URL + noColor)
                                    else:
                                        print("Unknown "+ URL)
                except:
                    print(dgrayColor + "Unable to open file " + arg)
                # clean up created file
                if os.path.exists("telescope.html"):
                    os.remove("telescope.html")
if __name__ == '__main__':
    main()