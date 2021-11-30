#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(text1):
    englishtran=language_translator.translate(text=text1,model_id='en-fr').get_result()
    e2f=englishtran.get("translations")[0].get("translation")
    return e2f

def frenchToEnglish(text2):
    frenchtran=language_translator.translate(text=text2,model_id='fr-en').get_result()
    f2e=frenchtran.get("translations")[0].get("translation")
    return f2e
