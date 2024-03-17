import os
import json
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

def load_search_terms(filename):
    """Lädt Suchanfragen aus einer Datei."""
    with open(filename, 'r', encoding='utf-8') as file:
        search_terms = file.readlines()
    # Entferne Leerzeichen und Zeilenumbrüche am Anfang und Ende jeder Suchanfrage
    search_terms = [term.strip() for term in search_terms]
    return search_terms

def get_search_results(search_term):
    """Ruft Suchergebnisse von Google ab und extrahiert relevante Texte."""
    links = []
    for link in search(search_term, tld="com", num=10, stop=10, pause=2):
        links.append(link)

    results = []
    for link in links:
        try:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.title.string if soup.title else "Kein Titel"

            text = ' '.join(re.sub(r'<[^>]+>', '', str(soup.get_text())).split())

            results.append({"title": title, "content": text, "url": link})
        except Exception as e:
            print(f"Fehler beim Abrufen von {link}: {e}")

    return results

def save_results(search_term, results):
    """Speichert die Suchergebnisse in einer Datei im JSON-Format."""
    with open(f"./results/{search_term.replace(' ', '_').replace('?', '_')}.json", 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

def web_crawler(filename):
    """Führt eine Web-Crawling-Suchanfrage für jede Suchanfrage in der Datei durch."""
    search_terms = load_search_terms(filename)
    os.makedirs("results", exist_ok=True)
    for search_term in search_terms:
        results = get_search_results(search_term)
        save_results(search_term, results)
        print(f"{len(results)} Ergebnisse für '{search_term}' gespeichert.")

# Beispielaufruf
web_crawler("search_terms.txt")
