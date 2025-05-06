# On-The-Go Connect4 and Pixel Art Frame – Django Server

This is the backend server for the **On-The-Go Connect4 and Pixel Art Frame**, built with **Django**. It provides APIs and data management for multiplayer games, pixel art sharing, and future online features.

🔗 **Project Page**: [View on Hackster.io](https://www.hackster.io/arvindsa/on-the-go-connect4-and-pixel-art-frame-48584d)  
👤 **Author Profile**: [Arvind S.A. on Hackster.io](https://www.hackster.io/arvindsa/)

## 📝 Description

This Django server supports the ESP32-based device by:

- Making a form that accepts a image url and sends it to mqtt for display on Connect4 pixel frame mode


## 🚀 Getting Started

1. **Clone this repository**
	```bash
	git clone <repo-url>
	cd <repo-folder>
	```
2. ** Install Dependencies**
	```
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
	```
3. ** Update MQTT Credientials** in pixelate/views.python
4. Runserver using `python manage.py runserver`, go to the url and send an image url
