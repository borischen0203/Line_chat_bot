# Line ChatBot for CS Conversion Programme Application Consultant

## Overview

Welcome to our Line ChatBot designed to assist aspiring students interested in the CS conversion programme application process. This ChatBot provides information, answers queries, and guides users through the application procedure for the Computer Science (CS) conversion programme.

## Getting Started

To use the Line ChatBot, follow these steps:

1. **Create Line Messaging API Account**: To set up the Line ChatBot, create a Line Messaging API account for your bot. Save the necessary credentials for later use.

2. **Set Up Virtual Environment**: Create a virtual environment in your preferred method based on your operating system (e.g., `virtualenv` or `venv`).

3. **Install Dependencies**: Activate the virtual environment and download all required packages listed in the `requirements.txt` file using the `pip install` command.

4. **Ngrok Setup**: Download the `ngrok` executable, a tool used to generate an HTTPS link that can be added to the webhook. In your terminal, run the command `ngrok http 8000` (assuming your localhost server runs on port 8000). The ngrok will generate an HTTPS link (e.g., `https://6a3b-2001-b400-e209-c92c-1d2e-53de-ca91-62b2.ngrok-free.app`) that you will use for the webhook.

5. **Webhook Configuration**: Configure the Line Messaging API webhook by appending `/line/webhook/` to your ngrok-generated HTTPS link. For example, if your ngrok HTTPS link is `https://6a3b-2001-b400-e209-c92c-1d2e-53de-ca91-62b2.ngrok-free.app`, the webhook URL will be `https://6a3b-2001-b400-e209-c92c-1d2e-53de-ca91-62b2.ngrok-free.app/line/webhook/`.

6. **Allow Hosts Configuration**: In your Django project's `settings.py`, add the ngrok-generated URL (without the `https://`) to the `ALLOWED_HOSTS` list. For example:
   ```
   ALLOWED_HOSTS = ['6a3b-2001-b400-e209-c92c-1d2e-53de-ca91-62b2.ngrok-free.app', '127.0.0.1']
   ```

7. **Run the Server**: In your terminal, run the command `python manage.py runserver` to start the Django development server.

8. **Add Line Account as Friend**: Add your Line ChatBot account as a friend and start interacting with it to seek guidance on the CS conversion programme application.

## Features

- **CS Programme Information**: The ChatBot provides comprehensive information about the CS conversion programme, help users to make a better decision.



## Disclaimer

Please note that while the ChatBot aims to provide helpful and accurate information, it is not a substitute for official guidance. Users should refer to the official CS conversion programme website and consult with the appropriate authorities for official and up-to-date information regarding the application process.

## Feedback and Contributions

We value your feedback and welcome contributions to enhance the functionality and accuracy of the ChatBot. If you encounter any issues or have suggestions for improvements, please feel free to reach out or submit pull requests.

Happy Chatting!
