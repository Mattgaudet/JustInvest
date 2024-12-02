## Setup
Clone the github repository https://github.com/Mattgaudet/JustInvest onto your machine, and run the file main.py.

## Roles
You can sign up users through the GUI, and they will be given the default Client role. To change a user's role you can change the passwd.txt file directly, or by logging in as an Admin role and using the GUI to modify user roles. The format for password file passwd.txt is: Username,PasswordHash,Role

Roles: Client, PremiumClient, Employee, FinancialAdvisor, FinancialPlanner, Teller, Admin

I have created a few example accounts for testing:
- Client account: username=client, password=Client12@
- Teller account: username=teller, password=Teller12@
- FinancialAdvisor account: username=FinAdv, password=FinAdv12@
- FinancialPlanner account: username=FPlan, password=FPlan12@
- Admin account: username=admin, password=Admin12@