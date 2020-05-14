$ErrorView = "NormalView"
$ErrorActionPreference = 'Break'
try {
          throw (new-object "Exception" @('foo'))
     } 
catch {
          write-host "caught failure: $_"
}
throw "Failed"
Write-Verbose -Message "Searching the Application Event Log."
