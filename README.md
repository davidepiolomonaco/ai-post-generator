# Academic Paper to LinkedIn Post Generator

This tool automatically searches for scholarly articles by a specific researcher and generates professional LinkedIn posts based on the selected articles.

## Features

- Search for researchers and their published papers using the Semantic Scholar API
- Select specific papers to create content for
- Generate professional LinkedIn posts using OpenAI's GPT models
- Save generated posts to a text file

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/davidepiolomonaco/ai-post-generator
   cd ai-post-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```
python3 main.py
```

The application will:
1. Prompt for your OpenAI API key (if not already stored)
2. Ask for the name of the researcher you want to search for
3. Display a list of papers authored by the researcher
4. Let you select which papers to generate LinkedIn posts for
5. Generate and save the posts to `output/posts.txt`


### How to Get an OpenAI API Key

1. Go to [OpenAI's platform website](https://platform.openai.com/signup)
2. Create an account or log in if you already have one
3. Navigate to the [API keys section](https://platform.openai.com/account/api-keys)
4. Click "Create new secret key"
5. Copy the generated API key (note that you won't be able to see it again)
6. Use this key when prompted by the application

## Project Structure

- `main.py`: Command-line interface and orchestration
- `article_search.py`: Handles searching for researchers and their papers
- `post_generation.py`: Generates LinkedIn posts using OpenAI's API

## Acknowledgments

This project uses:
- [Typer](https://typer.tiangolo.com/) for the command-line interface
- [OpenAI API](https://openai.com/api/) for generating content
- [Semantic Scholar API](https://api.semanticscholar.org/) for academic paper search