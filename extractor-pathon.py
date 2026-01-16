import pandas as pd
import requests
import msal

# ================= CONFIG =================
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
TENANT_ID = "YOUR_TENANT_ID"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]
GRAPH_URL = "https://graph.microsoft.com/v1.0"
# ==========================================

# Authenticate
app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

token = app.acquire_token_for_client(scopes=SCOPE)
access_token = token["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}

# Load CSV
df = pd.read_csv("sample.csv")

def get_manager(email):
    url = f"{GRAPH_URL}/users/{email}/manager"
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json().get("displayName", "")
    return ""

# Fetch managers
df["Manager"] = df["email"].apply(get_manager)

# Save output
df.to_csv("output_python.csv", index=False)

print("Python output written to output_python.csv")
