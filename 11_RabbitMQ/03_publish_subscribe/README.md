## Exchanges
1. What is Exchanges in RabbitMQ Architecture?
2. In producer, can it send a message directly to a queue? If it not send to queue, where it can send?
3. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all. Is it mean?
4. How can we control the exchange, and by what method?
5. Which commands to help us check all exchanges in RabbitMQ?
```bash
sudo rabbitmqctl list_exchanges
```

## Temporary queues
1. Firstly, let review a litte knowledge, do you remember how to all workers will consume the same queue or not?
2. What is keyword "share queue"? You want to share queue between workers or between producers and consumers?
3. In case logger at this tutorial, it need to hear about all log messages, not just a subset of them.

# Bindings
