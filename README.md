# IFBA KAFKA NEWS

## Execução
- **Docker**
    
        docker-compose up -d
- **Create topics**

        docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic news

        docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic main
- **Virtualenv**
    
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
- **Run services**

        python main_crawler.py
        python main_notices.py
        python main_main.py

# Testando tópicos manualmente

## Listar tópicos
```docker exec broker kafka-topics --bootstrap-server broker:9092 --list```

## Enviar mensagem para um tópico
```docker exec --interactive --tty broker kafka-console-producer --bootstrap-server broker:9092 --topic news```
CTRL+D para sair

## Ler mensagens do início de um tópico
```docker exec --interactive --tty broker kafka-console-consumer --bootstrap-server broker:9092 --topic news --from-beginning```

## Deletar um tópico
```docker exec broker kafka-topics --bootstrap-server broker:9092 --delete --topic quickstart```