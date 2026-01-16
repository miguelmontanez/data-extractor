# CSV Manager Lookup Tool (EntraAD / Microsoft Graph)

This project provides scripts to **enrich a CSV file** with the **manager information** from **EntraAD (Microsoft Graph)**. You can run it using **Python** or **PowerShell**, depending on your preference.

---

## Project Structure

```
extractor-pathon.py        # Python script to read CSV and fetch managers via Graph API
extractor-powershell.ps    # PowerShell script to read CSV and fetch managers via Graph API
sample.csv                 # Example CSV file with user data (emails in column C)
output.csv                 # Output CSV after running the scripts (Manager column added)
README.md                  # Project documentation
```

---

## Prerequisites

### Python

* Python 3.8+
* Required packages:

```bash
pip install pandas msal requests
```

### PowerShell

* PowerShell 7+
* Microsoft Graph module:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
```

---

## Configuration

### Python

Update the following variables in `extractor-pathon.py`:

```python
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
TENANT_ID = "YOUR_TENANT_ID"
```

### PowerShell

* Connect to Microsoft Graph before running the script:

```powershell
Connect-MgGraph -Scopes "User.Read.All","Directory.Read.All"
```

---

## Usage

### Python

```bash
python extractor-pathon.py
```

* Reads `sample.csv`
* Queries EntraAD for each email in column C
* Adds manager as **last column (N)**
* Writes `output.csv`

### PowerShell

```powershell
.\extractor-powershell.ps1
```

* Reads `sample.csv`
* Queries EntraAD for each email in column C
* Adds manager as **last column (N)**
* Writes `output.csv`

---

## Notes

* Users without a manager in EntraAD will have a **blank manager field**.
* Works with **hundreds of rows**; for very large CSVs, consider batching Graph API calls.
* Ensure proper permissions are granted in Azure AD to read user manager information.

---

## License

This project is for internal or client use. Ensure compliance with Microsoft Graph API licensing and organizational security policies.
