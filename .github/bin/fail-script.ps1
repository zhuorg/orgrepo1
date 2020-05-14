$ErrorView = "NormalView"
$ErrorActionPreference = 'break'
try {
          throw (new-object "Exception" @('foo'))
     } 
catch {
          write-host "caught failure: $_"
}
throw 'Test Error' ;
Write-Verbose -Message "Searching the Application Event Log."
