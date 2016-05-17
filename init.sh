#nginx conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#gunicorn conf
sudo ln -s /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
