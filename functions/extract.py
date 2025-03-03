"""Ce module contient les fonctions d'extraction de données d'une page web / regex mais pas d'une api."""

import re

"""
Extrait l'ID de la vidéo à partir de l'URL YouTube, y compris les shorts.
"""
def extract_video_id(url):
    regex = r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/[^/]+|(?:v|e(?:mbed)?|shorts)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None