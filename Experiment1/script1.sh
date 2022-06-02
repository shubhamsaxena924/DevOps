sudo yum update –y
sudo amazon-linux-extras install -y php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo groupadd www
sudo usermod -a -G www ec2-user
exit
