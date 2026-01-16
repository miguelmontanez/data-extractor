# Connect to Microsoft Graph
Connect-MgGraph -Scopes "User.Read.All","Directory.Read.All"

# Import CSV
$users = Import-Csv "sample.csv"

foreach ($user in $users) {
    try {
        $manager = Get-MgUserManager -UserId $user.email -ErrorAction Stop
        $user.Manager = $manager.AdditionalProperties.displayName
    } catch {
        $user.Manager = ""
    }
}

# Export CSV
$users | Export-Csv "output_powershell.csv" -NoTypeInformation

Write-Host "PowerShell output written to output_powershell.csv"
