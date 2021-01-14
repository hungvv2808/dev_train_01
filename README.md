# Docker tutorial #

- Docker/MySQL-Server document:
    + [How to run MySQL Docker container?](https://www.youtube.com/watch?v=NzKDlUVmIyE&t=210s)
    + [How to Do a Clean Restart of a Docker Instance](https://docs.tibco.com/pub/mash-local/4.1.1/doc/html/docker/GUID-BD850566-5B79-4915-987E-430FC38DAAE4.html)
    + [Change mysql password in Docker container](https://stackoverflow.com/questions/48249912/change-mysql-password-in-docker-container)

- Docker setup:

    + First step: Open command bash docker
    
            $ docker exec -it mysql bash
           
    + Second step: After access the docker bash use this command to login:
    
            mysql> mysql -uroot -p 
    
    + Last step: Enter password for mysql (1111)
    + Note: 
    
        - How to change password mysql
        + In mysql use this command to change root password:
        
                mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '1111';
                
        - Install Vim in docker bash
                
                $ yum install vim
        
        - Setup my.cnf follow url: /etd/mysql/my.cnf (create if not exists)
        
                $ vim my.cnf
                
                [mysqld]
                bind-address=0.0.0.0
                
        - Open mysql command to re-setup user/host/port
        
                mysql> CREATE USER 'root'@'%' IDENTIFIED BY '1111';
                
                mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
                
                mysql> FLUSH PRIVILEGES;
                

- Remove docker:
        
        $ sudo rm -Rf /Applications/Docker
        $ sudo rm -f /usr/local/bin/docker
        $ sudo rm -f /usr/local/bin/docker-machine
        $ sudo rm -f /usr/local/bin/docker-compose
        $ sudo rm -f /usr/local/bin/docker-credential-osxkeychain
        $ sudo rm -Rf ~/.docker
        $ sudo rm -Rf $HOME/Library/Containers/com.docker.docker

- That is all setup for docker/mysql follow and enjoy !!!