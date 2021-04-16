# azure-helper  
Just another repo about working with the azure cloud  

## Azure Policies  
It's possible to get the Account key of a storage account with this Azure ARM Template 'function'  
`listKeys(variables('auditStorageAccountId'), '2019-04-01').keys[0].value)`  
Change `0` to `1` to get the secondary key
