
try {
          throw (new-object "Exception" @('foo'));
          Write-Verbose -Message "Searching the Application Event Log."
     } 
catch {
          write-host "caught failure: $_"
}
throw 'Test Error haha' ;

