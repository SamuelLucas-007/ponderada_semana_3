# Para rodar a aplicação usei um ec2 em ubuntu e o processo foi o seguinte

1. Primeiro de tudo deve-se atualizar os pacotes
``` bash
sudo apt update
```
2. Em seguida deve-se instalar o pip
```bash
sudo apt install python3-pip
```
3. Clone e entre na pasta ponderada_semana_3
   
4. Instale o python venv
```bash
sudo apt install python3.10-venv
```
5. criar um ambiente virtual python com o venv
```bash
python3 -m venv venv/
```

6. Activate the virtual environment
Linux
```bash
source venv/bin/activate
```

7. For ubuntu, install the following packages
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config mysql-client-core-8.0
```

8. Install the requirements
```bash
pip install -r requirements.txt
```
9. Deve-se criar o database no rds da seguinte forma
```bash
mysql -h rds-endpoint -P your-port -u username -p
``` 
```bash
CREATE DATABASE ponderada;
``` 

```bash
exit;
``` 
10. Após isso, deve-se colocar a url do banco no arquivo __init__ e rodar as migrations para criar as tabelas
```bash
flask db init
``` 

```bash
flask db migrate
``` 

```bash
flask db upgrade
``` 

11.  Depois desses passos basta somente rodar a aplicação
```bash
python app.py
```

12. O endpoint seria o seguinte:
```bash
http://ec2.amazonaws.com:3000/api/ponderada/
```