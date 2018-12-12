import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

imgurl = "https://thefertilechickonline.com/wp-content/uploads/2017/12/mengroup.jpg"
imgbytes = image_helpers.get_image_from_url(imgurl)

rekesp = client.detect_faces(Image={'Bytes':imgbytes},Attributes=['ALL'])
pprint(rekesp)
print(len(rekesp['FaceDetails']))



