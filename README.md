# Avaliação CFI - API

## Requisitos

* Python 3.6.*
* Virtualenv +15.1.0
* Pip +9.0.1 (python3)

## Configuração

### CORS

Configurar as URL do front-end para impedir que os browsers rejeitem as requisições.

Em AvaliacaoCIF/settings.py, adicionar a URL em CORS_ORIGIN_WHITELIST

## Instalação

Criar e iniciar o ambiente virtual

```console
user@server:~$ virtualenv -p python3 .env
user@server:~$ source .env/bin/activate
```

Instalar dependências

```console
user@server:~$ pip3 -r requirements.txt
```

Preparar base de dados

```console
user@server:~$ python3 manage.py migrate
```

Criar usuário com poderes de administração do sistema

```console
user@server:~$ python3 manage.py createsuperuser
...
```

Iniciar 

```console
user@server:~$ python3 manage.py runserver
```
