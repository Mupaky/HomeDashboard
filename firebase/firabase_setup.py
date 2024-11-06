# firebase_setup.py

import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access Firebase configuration from environment variables
firebase_key_path = os.getenv("FIREBASE_ADMINSDK_KEY_PATH")
firebase_project_id = os.getenv("FIREBASE_PROJECT_ID")
firebase_api_key = os.getenv("FIREBASE_API_KEY")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred, {
    'projectId': firebase_project_id,
})

# Initialize Firestore client
db = firestore.client()
