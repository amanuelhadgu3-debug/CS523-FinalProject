from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = [101,102,103,104,105,106,107,108]

while True:

    order = {
        "order_id": random.randint(1000, 9999),
        "product_id": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(50, 3000), 2)
    }

    producer.send("ecommerce-orders", order)

    print("Sent:", order)

    time.sleep(1)