# MissionEd

MissionEd is a Placement Portal module as an open-source Odoo Extension.
The missioned module is maintained in parallel to odoo source-code and included in the add-ons.

-> PLace the Odoo source folder appropiately in this tree format:

___ app
     |___ custom
     |      |___ missioned
     |
     |___ odoo-15.0


-> Run the following command to build/update the missoned module:

cd app/odoo-15.0
./odoo-bin --addons-path=../custom,addons -d mydb -u missioned

-> Module metadata:        custom/missioned/__manifest__.py
   Main(index) file:       custom/missioned/__init__.py
   UI dir:                 custom/missioned/views
   Models dir:             custom/missioned/models
