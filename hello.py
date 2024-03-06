
from gradientai import Gradient
import os
import requests
import html2text
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

COLLECTIONID = st.secrets.GRADIENT_COLLECTION_ID
WORKSPACEID = st.secrets.GRADIENT_WORKSPACE_ID
AUTHORIZATION = st.secrets.GRADIENT_ACCESS_TOKEN

os.environ['GRADIENT_COLLECTION_ID'] == st.secrets['GRADIENT_COLLECTION_ID']
os.environ['GRADIENT_WORKSPACE_ID'] == st.secrets['GRADIENT_WORKSPACE_ID']
os.environ['GRADIENT_ACCESS_TOKEN'] == st.secrets['GRADIENT_ACCESS_TOKEN']

def main() -> None:
	#gradient = Gradient()
	#base_model = gradient.get_base_model(base_model_slug="mixtral-8x7b-instruct")
	st.title ('Uganda Law Chatbot')
	question = st.text_input ('Ask a question:')

	url = "https://api.gradient.ai/api/blocks/answer"

	if question:
	
		payload = {
    			"source": {
        		"type": "rag",
        		"collectionId": COLLECTIONID
    				},
    			"question": question
			}
		headers = {
    			"accept": "application/json",
    			"x-gradient-workspace-id": WORKSPACEID,
    			"content-type": "application/json",
    			"authorization": AUTHORIZATION
			}
		
		response = requests.post(url, json=payload, headers=headers)

		output = html2text.html2text(response.text)

		st.write(output)

if __name__ == "__main__":
	main()