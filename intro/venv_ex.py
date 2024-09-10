print("inside main")
"""
venv:
virtual environment
סביבה וירטואלית
זה כלי שמאפשר לנהל את התלויות שלי ברמת הפרוייקט
כדי לוודא שכל פרוייקט רץ בסביבה נפרדת


how to create ven
syntax:
python -m venv <env_name>
example:

python -m venv my_venv
this will crate

linux / windows
bin/ / scripts/ - all the scripts (interpreter, pip)
include/ - including the C header files to run C
lib/ - the standard library files
pyvenv.cfg - the configuration file

step 2:
activate the venv
windows: <env_name>\Scripts\activate
windows: my_venv\Scripts\activate
linux: source <env_name>/bin/activate
linux: source my_vev/bin/activate


step 2/1:
deactivate (activate again if you want to work)

step 3:
install required packages (depending the business)
example:
pip install requests
now, the new installed package will be in /lib


step 4:
pip list
will display all pacakges installed

step 5:
create a requirements file
pip freeze > requirements.txt


step 6: 
install the requirements file

pip install -r requirements.txt

"""


