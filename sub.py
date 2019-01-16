import time
import sys

from google.cloud import pubsub_v1


def sub(project_id, subscription_name):

    client = pubsub_v1.SubscriberClient()
    subscription_path = client.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        # we must "acknowledge," otherwise they will be redelivered
        message.ack()

    client.subscribe(subscription_path, callback=callback)
    print('Listening for messages on {}'.format(subscription_path))

    while True:
        # The subscriber is non-blocking. We must keep the main thread from
        # exiting so it can process messages asynchronously in the background.
        time.sleep(60)


if __name__ == '__main__':

    _, p, s = sys.argv
    sub(p,s)
