from kafka import KafkaProducer
from time import sleep
from recordbuilder import RecordBuilder
from temp import temp

if __name__ == '__main__':
    THREAD_SLEEP_DURATION = 1
    KAFKA_TOPIC = 'fryns-input'
    PLATFORM_URL = 'apachekafka-a6909623a228.victhorious.com:9091'

    producer = KafkaProducer(bootstrap_servers=PLATFORM_URL)

    while True:
        temperatuur_sensor_1_grote_alambiek = temp.measure()

        print(temperatuur_sensor_1_grote_alambiek)

        grote_alambiek_record_builder = RecordBuilder()
        grote_alambiek_record_builder.add_tag('name', 'groteAlambiek') \
            .add_field('temperatuurSensor1', temperatuur_sensor_1_grote_alambiek)
        
        grote_alambiek_record = grote_alambiek_record_builder.get_record()

        encoding = 'utf-8'
        producer.send(KAFKA_TOPIC, grote_alambiek_record.encode(encoding))

        sleep(THREAD_SLEEP_DURATION)
