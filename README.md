# Health Advice Chatbot

## Overview
This project is a simple chatbot that leverages OpenAI's GPT-3.5-turbo model to provide preliminary health advice based on natural language queries. Note that this chatbot is not a substitute for professional medical advice.

## Features
- Symptom Checker: Get potential conditions based on symptoms described.
- Preventive Measures: Get advice on preventive measures for various health concerns.
- General Health Advice: Receive general health tips and advice.
- Medical Terms: Get explanations for medical terms.
- First Aid: Get first aid tips for various conditions.

## Demo
[![Health Advice Chatbot Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID)

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/health-advice-chatbot.git
    cd health-advice-chatbot
    ```

2. **Install Dependencies:**
    Make sure you have Python and pip installed. Then run:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key:**
    - Get your API key from OpenAI.
    - Create a file named `.env` in the project root and add your API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application:**
    ```sh
    streamlit run app.py
    ```

## Usage
1. Open the application in your browser (usually at `http://localhost:8501`).
2. Select the type of query from the dropdown menu.
3. Enter your query in the text area.
4. Click the "Submit" button to get a response.

## Error Handling and Troubleshooting

### Common Issues:
- **RateLimitError:** You have exceeded your current quota. Please check your plan and billing details.
- **InvalidRequestError:** There was an issue with your request, likely due to invalid parameters or incorrect API key.
- **Network Issues:** Ensure you have a stable internet connection.

### Solutions:
- **Retry Logic:** The application has built-in retry logic for handling temporary rate limits. If the error persists, consider checking your OpenAI plan and usage.
- **API Key:** Ensure your API key is correct and has the necessary permissions.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or support, please open an issue in the repository or contact the project maintainer at your-email@example.com.
