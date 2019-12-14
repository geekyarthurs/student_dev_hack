import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys
authenticator = IAMAuthenticator('<API KEY HERE>')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
  
visual_recognition.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')
def detect_image(imagePath):  
    with open(imagePath, 'rb') as images_file:
     classes = visual_recognition.classify(
            images_file=images_file,
         threshold='0.3',
         classifier_ids='food'

        ).get_result()
  
      #["images"][0]["classifiers"][0]["classes"]
  
    return classes
                         
