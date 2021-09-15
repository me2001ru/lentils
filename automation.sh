#!/bin/bash/

# Create Ubuntu, Linux machine

#Login and run :
sudo apt-get update
sudo apt-get install apache2 -y

apache2 —version 	# to check the version on apache installed

# Configure Firewall
# ufw app list				# check if apache is in the list
ufw allow ‘Apache’		# to let apache go through the firewall

# Check if service is running
sudo systemctl start apache2
sudo systemctl enable apache2

# Install few libraries
sudo apt-get install libapache2-mod-wsgi python-dev -y

# Setup directories & get into right directory where flask application will be placed
cd /var/www/; mkdir webApp; cd webApp; mkdir webApp

sudo apt-get install python-pip	-y # installs pip
pip install flask
pip install flask_sqlalchemy

#Move the project from localhost to remote host
scp /User/meru/Desktop/lentils/ ubuntu@10.0.2.15:/var/www/webApp/

#Setup virtualhost (config file) - ip is set to 127.0.0.1
scp /User/meru/Desktop/lentils/webApp.conf ubuntu@10.0.2.15:/etc/apache2/sites-available/webApp.conf

# Activate this
sudo a2ensite webApp
sudo systemctl reload apache2

cd /var/www/webApp

#Move wsgi file from localhost to remote host
scp /User/meru/Desktop/lentils/webapp.wsgi ubuntu@10.0.2.15:/var/www/webApp/webapp.wsgi

# Configure the changes
sudo service apache2 restart
