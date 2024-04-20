# OllamaLit-Llama-3: Research Paper Summarization with Ollama, Llama-3 & Streamlit

## Motivation
Summarizing research papers can be a time-consuming task, especially when dealing with lengthy and complex papers. This project aims to automate the process of research paper summarization using state-of-the-art language models, specifically Ollama and Llama-3. By leveraging these powerful models and integrating them with a user-friendly Streamlit interface, researchers and academics can quickly generate concise summaries of research papers, saving valuable time and effort.

## Features
- Upload research papers in PDF or TXT format
- Select from two language models: GPT-3.5-turbo or text-davinci-003
- Generate concise summaries of research papers
- Interactive chat interface for easy interaction with the language model
- Track conversation history and associated costs
- Clear conversation history to start fresh

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/ollamalit-llama-3.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the Ollama library with your API key:
   ```
   oai.api_key = "YOUR_API_KEY"
   ```

## Usage
1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Upload a research paper in PDF or TXT format using the file uploader.

3. Select the desired language model from the sidebar (GPT-3.5-turbo or text-davinci-003).

4. Click the "Summarize" button to generate a summary of the uploaded research paper.

5. View the original research paper text and the generated summary.

6. Interact with the language model using the chat interface to ask questions or provide additional context.

7. Track the conversation history, model usage, and associated costs in the sidebar.

8. Use the "Clear Conversation" button in the sidebar to reset the conversation history and start fresh.

## Repository Overview
```
├── app.py                  # Streamlit app main file
├── requirements.txt        # Required dependencies
├── README.md               # Project README
└── assets/                 # Directory for storing assets (e.g., images)
```

## Future Enhancements
- Support for additional file formats (e.g., DOCX, HTML)
- Customizable summarization parameters (e.g., summary length, abstractiveness)
- Integration with academic databases for seamless paper retrieval
- Batch processing of multiple research papers
- Export functionality for generated summaries (e.g., PDF, TXT)

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. For major changes, please discuss them first in the issues section.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [Ollama](https://github.com/ollama-ai/ollama) - Open LLM for Lightweight Architectures
- [Llama-3](https://github.com/facebookresearch/llama) - Open and Efficient LLM developed by Facebook Research
- [Streamlit](https://streamlit.io/) - Open-source app framework for machine learning and data science

## Contact
For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
