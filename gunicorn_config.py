# gunicorn_config.py

bind = '0.0.0.0:8000'  # O endereço e a porta em que o Gunicorn irá escutar
workers = 3  # Número de trabalhadores (processos de trabalho)
accesslog = '-'  # Log de acesso padrão (impressão no stdout)
errorlog = '-'  # Log de erro padrão (impressão no stdout)
loglevel = 'info'  # Nível de log
