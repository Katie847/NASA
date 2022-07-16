from urllib import response
import requests
import pprint
import shutil # to save it locally

#this script locally saves images from NASA's James_Webb album by accessing the API
#make an API request using the album endpoint from the pics and videos API. Save data as a Python dic.
endpoint = "https://images-api.nasa.gov/album/James_Webb_First_Images"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key}
response = requests.get(endpoint, params=query_params)

photos = response.json()

def picfiles():
    ## Set up the image URL and filename
    filename = pic_url.split("/")[-1]  # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(pic_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

#.jpg extraction solution = photos['collection']['items'][::]['links'][0]['href']

items = photos['collection'] ['items']

# save each picture by using .jpg url for each item
for item in range(len(items)):
    pic_url = (items[item]['links'][0]['href'])

    picfiles()  