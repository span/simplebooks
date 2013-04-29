This is a small web application that can be used to add verifications when doing your taxes. It uses Python and the Django web framework. To run this 
example you need access to a mysql database and a server that can serve django web applications. Check out /simplebooks/settings.py for database 
information.

If you only want to view the source of the actual web app, see the /simplebooksform/ folder. It contains the models, url's, views and templates that 
are used.

Current features
------------------
* Add a verification
* View all verfications
* Filter verifications by title with search
* View results
* File upload to store invoice

Note that the only accounts that are supported at the moment are "income" and "expense". In future versions the account will auto complete and I plan 
to add support for account numbers as well.

Planned features
-----------------
* Custom accounts
* Autocomplete on accounts
* Account results overview
* Handle different years
* Pie charts!
