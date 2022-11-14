# cademed-back
Repositorio do backend do sistema CadêMed

# EXECUTAR O BACK
-> Basta criar um ambiente virtual dentro da pasta back end é importando colocar a venv dentro do gitignore;

-> Depois executa o comando:  
pip install -r requirements.txt

-> E em seguida voce executa outro comando que é o : 
python manage.py migrate

-> E pronto, so rodar o server : 
python manage.py runserver 

-> E tem que ter o banco de dados tambem (Usar o MySQL - e criar o banco de dados com o nome: cademed) 

# Quem tiver usando windows para resolver esse problema (modulo curses Not found), caso taambém passem por ele, é só usar esse comando na linha de comando:
pip install windows-curses

_Nota do Ivan sobre o problema: O modulo curses é mais usado em ambientes Unix, portanto no windows não é suportado. Mas a comunidade python implementou esse binario não oficial para poder também usar no windows. Boa sorte! E espero ter ajudado.  :D_

# Caso apareça um erro Django_filters execute o seguinte codigo:
pip install django-filter

_Nota do Ivan sobre o problema: O módulo django-filter não é nativo do python3 por isso tem que ser importado a parte._