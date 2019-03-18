from kafka import KafkaProducer
from time import sleep
from recordbuilder import RecordBuilder


if __name__ == '__main__':
    # Constante waardes
    THREAD_SLEEP_DURATION = 1
    KAFKA_TOPIC = 'fryns-input'
    PLATFORM_URL = 'apachekafka-a6909623a228.victhorious.com:9091'

    # Kafka data producer, met producer.send (zie beneden)
    # wordt de data naar onze apache kafka server doorgestuurd
    producer = KafkaProducer(bootstrap_servers=PLATFORM_URL)

    while True:
        # Maak een RecordBuilder aan en voeg InfluxDB tags en fields
        # toe met add_tag en add_field.
        alambiek1_record_builder = RecordBuilder()
        alambiek1_record_builder.add_tag('name', 'alambiek1') \
            .add_field('temperatuurSensor1', 50) \
            .add_field('temperatuurSensor2', 60) \
            .add_field('drukSensor1', 1.3) \
            .add_field('laagWaterNiveau', False)

        # Eens dat alle fields en tags ingevuld zijn, doe
        # get_record. Dit returned de record als een JSON string
        # die op zo een manier gestructureerd is dat chiel en ik
        # hem heel gemakkelijk verder kunnen gebruiken.
        alambiek1_record = alambiek1_record_builder.get_record()

        # Hetzelfde maar dan voor de andere alambiek.
        # We hebben het graag als de meetwaardes van de twee
        # alambieken uiteengehouden worden door een InfluxDB tag.
        alambiek2_record_builder = RecordBuilder()
        alambiek2_record_builder.add_tag('name', 'alambiek2') \
            .add_field('temperatuurSensor1', 50) \
            .add_field('temperatuurSensor2', 60) \
            .add_field('drukSensor1', 1.3) \
            .add_field('laagWaterNiveau', False)
        alambiek2_record_builder = RecordBuilder()

        alambiek2_record = alambiek2_record_builder.get_record()

        # Verstuur de records naar onze apache kafka
        # Vanuit hier zorgen Chiel en ik ervoor dat de data in
        # een InfluxDB en Grafana dashboard terecht komt.
        encoding = 'utf-8'
        producer.send(KAFKA_TOPIC, alambiek1_record.encode(encoding))
        producer.send(KAFKA_TOPIC, alambiek2_record.encode(encoding))
        print("test")
        sleep(THREAD_SLEEP_DURATION)
