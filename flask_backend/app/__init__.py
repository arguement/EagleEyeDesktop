from flask import Flask
from firebase_admin import credentials, firestore, initialize_app
import json,os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(__name__)
# Initialize Firestore DB

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "capstone-5515a",
  "private_key_id": "43d732721893bf606a54d24c7e8915e8cf3d4e7a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDJ8Z1/1mobENN6\n1JQU6QR7lUBKaNvuKMIrDOEAa60yu9BmobMeAMxcGJMDXi3caxhDJe1AeBFIuKxZ\nZZsD4snPa4kDfW5HEGF3kKeSp/HIIDIsJEMbInACylSQv6oO59D2+aeMNRAYpWFk\nAys8l8jNIM6MPKiZ0r8AjcbwXBUwQJeL+X7W0mf0a+dBPVST5diyCjWphYtNMZMs\nD/QicwiSyWjjQ3VNZVPJj/is0ATyJjqJHqLRgUMOVkKfKMT6xu+Ffx/mV1Z/5YhE\nnLeIFW2FMLvbfWLuR6OJnEqqaM1N/fKSqbNC12LpLSCbv4CW8nUuHsZSwcpKrh/T\nrINBSgRDAgMBAAECgf8vzIQ80si5Wh+fpyAnjbPwoUeBoWvwoDGoX9K4i/SAwZLl\na+sVSp6KGTkhrp6vxNMb7xx+Qaf/LakvERUHyJiGZFVxvEyHcM7Dw2uvPQpefa8d\nTgJc5mILkySoanA3CSRRUQuVtYP+J+i77P0sU4K3a845mrox5gM0Aq3xWSZ6UsRy\npvMgU1GMcrEG5TJKduijtesXDm5d1pCqgiXyZ7fI/fjF5UvS6e2IsP8PgZb/bElr\nQSt4ugYOoaPNW48dxnCsC3zGAWzkH4SCqI3z2y1h72L1N4CSTOR2H8w+9gRTEUQJ\nkpulfc3C6iobEcpxDvl5PAqF4Pw1Cs5KsH3Ht6ECgYEA91qbhblv8B+HGGv/Z60z\nEa2VREBLRD4skrm1ylOXib6y4SzLLschO5v2OHJzq+Kat36uqAaTDFGOK8zrFfgE\nvLNkeNW22ereY3Yvmg63ZBoyEGwk68CLrY07+aDv1eKXgfaYx5vM+Ln6/EWwBYLh\nnQVhazjxrZQGTTCMrc7zBksCgYEA0QCqR+ybgfR7M3pFM++qvY6+LQ7Jbn4CqgyI\nR2Y1+ZJJkdcAUYdvKbKieOIknmkgATJIuZveE67S9e50czs84QCyh0pDKGiTsKGb\nisr8i9W9E3Olw+Qe00Czt5vY6Yn81pbs2iuH0+DMmm4UB05dh88/+ifaaU9RVKba\n++JFnukCgYB2XlPCYIUiwdOiajwk3wtrUEf4C1R5ac9mv5wxIGOKNUng29C3p+9N\nWUswpASaoqwrV2I5YjwITxbb+woczz1lF+vir1L7YZveuPX6oUQ9kROYLEhW0SOG\nf+nNgaiEEBU0yk8+Zl5mQInNI4Qifwl8XNDLwMpWqFmDotIPctN1lQKBgHKAKsm8\nlnVbuyM4mTEa3C99RDLrJu+hmVQQCZkUJf3UZvm/EC2aRQxTES+otOcUMLR3F+CX\nw9KEtI6HVMTMb03VU/lKdgBtSnw6DTy8eB8jubIuaWIoV7rkd5DfkLZhImNty9S6\nhG9PeMgiBlb6V8NPh31E2CNZkPUPdGkKTZoBAoGAL4inzfbi0ZjPznaiYwe2dpWX\nOYgnpxoxt8sHtoVfnR3Ae9uqLMOYPMFeB42lYjT3fBQ0kef09LzgjBfkaxEftebB\n89HxMwln7HDfpB18+Kb4yCVcECWHb3EmfVdT/Fbsc+ykDTD53y9+A1GwrT/QMz+u\nnYNZA/fPNLXgAs6BF8Q=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-r6otb@capstone-5515a.iam.gserviceaccount.com",
  "client_id": "115224119715530321246",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r6otb%40capstone-5515a.iam.gserviceaccount.com"
}
)

default_app = initialize_app(cred)
db = firestore.client()

users = db.collection('User')
reports = db.collection('Crime Report')
priorities = db.collection('Crime Priorities')
police_officers=db.collection('Police Officer')

from app import views