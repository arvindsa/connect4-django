import json

from django.shortcuts import render
from .forms import URLForm
from .utils import (
    pixelate_image_inline,
)  # assuming you save the function in pixelate/utils.py
import paho.mqtt.client as mqtt
import json
import ssl


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")


def publish_to_mqtt(json_data):
    # MQTT connection details
    mqtt_broker = "d970b1e5.ala.asia-southeast1.emqxsl.com"
    mqtt_port = 8883
    mqtt_topic = "device/esp32/commands"  # Adjust topic as needed
    mqtt_username = "test1"  # If required
    mqtt_password = "test1"  # If required

    # Create MQTT client
    client = mqtt.Client()

    # Set username and password if needed (optional)
    if mqtt_username and mqtt_password:
        client.username_pw_set(mqtt_username, mqtt_password)

    # Set TLS/SSL connection
    client.tls_set_context(ssl.create_default_context())
    client.tls_insecure_set(True)  # Ignore SSL certificate verification (optional)

    # Connect to the MQTT broker
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(mqtt_broker, mqtt_port, 60)

    # Publish JSON data
    payload = json.dumps(json_data)  # Convert dict to JSON string
    client.loop_start()
    client.publish(mqtt_topic, payload, qos=1)  # Publish to topic with QoS 1
    client.loop_stop()
    client.disconnect()


# def process_image_and_send_mqtt(url):
    # # Your image processing function here
    # json_data = pixelate_image(url)  # Assuming pixelate_image returns the JSON data
    #
    # # Now send this JSON data to MQTT
    # publish_to_mqtt(json_data)
    #
    # return json_data  # Return JSON to display in template

def pixelate_view(request):
    result_html = None
    json_data = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["image_url"]
            try:
                result_html, json_data = pixelate_image_inline(url, n=7)
                publish_to_mqtt(json_data)
            except Exception as e:
                result_html = f"<p style='color:red;'>Error processing image: {e}</p>"
    else:
        form = URLForm()

    return render(
        request,
        "pixelate_form.html",
        {
            "form": form,
            "result_html": result_html,
            "json_data": json_data,
            "json_string": json.dumps(json_data),
        },
    )
