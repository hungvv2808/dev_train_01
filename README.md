Python Train

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
                

- That is all setup for docker/mysql follow and enjoy !!!