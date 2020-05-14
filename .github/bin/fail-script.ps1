#$ErrorView = "NormalView"
$ErrorActionPreference = 'Stop'
try {
          throw (new-object "Exception" @('foo'))
     } 
catch {
          write-host "caught failure: $_"
}
throw "Failed"
Write-Verbose -Message "Searching the Application Event Log."
