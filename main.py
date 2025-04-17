import typer
from article_search import search_articles
from post_generation import generate_post
from pathlib import Path

app = typer.Typer()
@app.command()

def save_api_key(api_key: str):
    env_path = Path(".env")
    with env_path.open("w", encoding="utf-8") as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")


def start():
     if not Path(".env").exists():
        api_key = typer.prompt("Inserisci la tua chiave API di OpenAI: ")
        save_api_key(api_key)
    
     researcher = typer.prompt("Inserisci il nome del ricercatore: ")
     articles = search_articles(researcher)
     
     if not articles:
         typer.echo("Nessun articolo trovato.")
         raise typer.Exit()
     else:
        typer.echo(f"Articoli trovati per {researcher}: ")
        for idx, article in enumerate(articles, start=1):
            typer.echo(f"{idx}. {article}")
    
     selected_article = typer.prompt("Inserisci il numero dell'articolo da visualizzare: ")
     if not selected_article: 
         typer.echo("Nessun articolo selezionato! Uscita...")
         raise typer.Exit()
     
     OUTPUT_PATH = Path("output/posts.txt")
     OUTPUT_PATH.parent.mkdir(exist_ok=True)
     with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for article in selected_article:
            post = generate_post(article)
            f.write(post + "\n\n")
        typer.echo(f"Post generato e salvato in {OUTPUT_PATH}")

     
if __name__ == "__main__":
    start()