# Criando, configurando e iniciando seu projeto Django 

 ## ⚙️ Instalação
<p>
1. Intstale o Python3.11 </br>
<code>brew install python@3.11</code>
</p>

<p>
2. Instale o virtualenvwrapper: </br>
<code>brew install virtualenvwrapper</code>
</p>

<p>
3. Crie o ambiente virtual: </br>
<code>mkvirtualenv -p python3.11 env_[name_project]</code>
</p>

<p>
4. Set o ambiente virtual para o projeto: </br>
<code>setvirtualenvproject env_[name_project] [dir_name_project] </code>
</p>

<p>
5. Para iniciar o desenvolvimento: </br>
<code>workon env_[name_project]</code>
</p>

<p>
6. Crie um arquivo venv.sh e add as envs com o formato abaixo: </br>
</p>
 
 ```bash
export STUDENT_ENV='local'
 ```

<p>
7. Iniciando o venv.sh: </br>
<code>source venv.sh</code>
</p>

<p>
8. Upgrade pip: </br>
<code>pip install --upgrade pip</code>
</p>

<p>
9. Requirements ou install-req: </br>
<code>pip install -r requirements.txt</code></br>
ou se tiver o arquivo install-req</br>
<code>pip install -r install-req.txt</code>
</p>

 ## 🚀 Start project
 Para iniciar o seu projeto e começar a rodar a aplicação na sua máquina siga as seguintes linhas de comando no seu terminal:

<code>python manage.py makemigrations</code></br>
<code>python manage.py migrate</code></br>
<code>python manage.py collectstatic --noinput</code></br>
<code>python manage.py createsuperuser</code></br>
<code>python manage.py runserver</code></br>

<p>
10. Para sair do projeto: </br>
<code>deactivate</code>
</p>