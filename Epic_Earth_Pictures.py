from urllib import response
import requests
import shutil # to save it locally

#Uses Epic API to locally download the most recent available Epic pictures of Earth

endpoint = "https://epic.gsfc.nasa.gov/api/natural"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key}
response = requests.get(endpoint, params=query_params)

photos = response.json()
print(f'Found {len(photos)} photos')

#photos = (photos[0])
print(type(photos))
#print(photos.get('image'))

#print(photos.get('camera'))
#print((photos.keys()))

def picfiles():
    ## Set up the image URL and filename
    filename = pic_url.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content.
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

#write url for each image using the date and image data
for photo in photos:
    image = (photo['image'])
#https://epic.gsfc.nasa.gov/archive/natural/2022/01/29/png/epic_1b_20220129042159.png
    date = photo['date']
    date = (date[0:10])
    date = map(lambda x: x.replace('-', '/'), date)
    date = ("".join(date))
    pic_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image}.png"

    #picfiles()
