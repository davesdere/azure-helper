# azure-helper  
Just another repo about working with the azure cloud  

## Azure Policies  
Policies can be composed of 3 components;  
- Initiatives are a regroupment of policies (Ms calls them PolicySet in the technical doc)  
- Definitions describe what we want to `audit` (or `auditIfNotExists`), remediate(`deployIfNotExists`) or `deny`.  
  - It must contains a `if/then` section.  
- Assignments are what "enables" the policy definition at a certain scope.  
N.B. that **Policies** and **Assignments** can be deployed at different scopes as well as assignments but definition must be at same or parent level than the assignment.  
TODO: Add a diagram

## ARM Tips  
It's possible to get the Account key of a storage account with this Azure ARM Template 'function'  
`listKeys(variables('auditStorageAccountId'), '2019-04-01').keys[0].value)`  
Change `0` to `1` to get the secondary key
