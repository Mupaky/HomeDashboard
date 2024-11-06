# firebase_setup.py

import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the path to the Firebase admin SDK key file from the environment variable
firebase_key_path = os.getenv("FIREBASE_ADMINSDK_KEY_PATH")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()
