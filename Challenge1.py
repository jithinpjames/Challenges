import requests
from bs4 import BeautifulSoup
import os

def file_write(content):
    """" Method to write response content to output html file and text file
         Accepts response contents and writes to HTML and text file in same directory
    """
    with open ('Challenge1.html','w') as file:
        file.write(content)
        path1 = os.path.join(os.getcwd(),'Challenge1.html')
    with open ('Challenge1.txt','w') as file:
        file.write(content)
        path2 = os.path.join(os.getcwd(),'Challenge1.html')
        print('Add to cart success,please verify the cart details from html file : - %s or text file : - %s' %(path1,path2))

def get_data(resp):
    """" Builds data required for the post request as a dictionary
         Accepts response object and returns data dictionary
    """
    soup = BeautifulSoup(resp.content,'html.parser')
    
    CSRFToken = soup.find('input',attrs={'name':'CSRFToken'})['value']
    baseProductCode = soup.find('input',attrs={'name':'baseProductCode'})['value']
    productCodePost = soup.find('input',attrs={'class':'variantSizeCode'})['value']

    data={'qty':1,'baseProductCode':baseProductCode,'productCodePost':productCodePost,'CSRFToken':CSRFToken}
    return data

def api_calls(url):
    """" Creates a session and does all required Api calls 
         Accepts product URL page and returns status
    """
    s = requests.session()
    resp1 = s.get(url)
    if resp1.status_code == 200:
        data = get_data(resp1)
        resp2 = s.post('https://www.shoppersstop.com/cart/add',data=data)
        print("Response from add to cart API Call : - %s" %resp2.status_code)
        resp3 = s.get('https://www.shoppersstop.com/cart')
        print('Response from get cart details API Call : - %s' %resp3.status_code)
        if  resp2.status_code == 200 and resp3.status_code == 200:
            file_write(resp3.text)
        else:
            print('Add to cart failed due to Api error, please check the URL provided or contact Jithin:9742037425')
    else:
        print('URL Error, please check the URL provided or contact Jithin:9742037425')



if __name__ == '__main__':
    url = input('Enter the URL here : - ')
    api_calls(url)
    user_input = input("Press enter to exit ")
