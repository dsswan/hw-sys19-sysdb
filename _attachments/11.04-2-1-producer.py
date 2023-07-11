#!/usr/bin/env python3
# coding=utf-8
import pika

credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='158.160.55.54', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
