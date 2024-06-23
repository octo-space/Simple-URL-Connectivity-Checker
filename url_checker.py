import urllib.request as urlre

print("Site Connectivity Checker ")

url = input("Enter Url : ")

def urlCheck():
    try:
        res = urlre.urlopen(url)
        print(f'Status Code: {res.getcode()}')
    except Exception as e:
        print(f'Error occurred: {e}')

urlCheck()
