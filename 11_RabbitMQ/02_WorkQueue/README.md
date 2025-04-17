## What This Tutorial Focuses On
1. How one queue can be consumed by many worker? How to define that rules?

## Round-robin dispatching
1. What is a algorithm for worker?
2. How to change another algorithm to increase effective queue?

## Message acknowledgment
1. what happens if a consumer start a long task and it terminates before it completes?
2. For a long task on worker, what happens if we terminate a worker? In normal usage RabbitMQ, how it handle it?
3. How to handle which messages is lost?
4. How to make sure that a message will be never lost?
5. What is mechanism to handle for a died worker? Message will re-queue or not?
6. What time of timeout occur in case lost messages?
7. Why we need setting a timeout in case lost messages?
8. Do you understand about keyword auto_ack=True in callback function? How to change another operation?
9. Suppose 1 acknowledgement sent on the same channel and received the delivery,
 then you try to using a different channel will catch acknowledge? What happens in this cases?
10. 

## Forgotten acknowledgment
1. A serious problem will occured if you forget to handle an acknowledgement? Which problems will happen?
2. Suppose you know that you maybe forget to handle a forgotten ack, how we can check it? Demonstrate that you already handled it?
```bash
sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
```
3. 

## Message durability