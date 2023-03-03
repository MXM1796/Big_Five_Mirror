import os
import google_auth_oauthlib
import requests
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
import pandas as pd
import numpy as np

# Pakete für Youtube Video Transkripte
from youtube_transcript_api import YouTubeTranscriptApi


def youtube_api_connector(video_id):
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)

    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )

    return request.execute()

def data_source(video_id):
    response = youtube_api_connector(video_id)

    response_dict = {}

    response_dict["video_id"] = response["items"][0]["id"]
    response_dict["test"] = response["items"][0]["snippet"]["title"]
    response_dict["viewCount"] = response["items"][0]["statistics"]["viewCount"]
    response_dict["likeCount"] = response["items"][0]["statistics"]["likeCount"]
    response_dict["commentCount"] = response["items"][0]["statistics"]["commentCount"]
    response_dict["title"] = response["items"][0]["snippet"]["title"]
    response_dict["description"] = response["items"][0]["snippet"]["description"]
    response_dict["channelTitle"] = response["items"][0]["snippet"]["channelTitle"]
    response_dict["tags"] = response["items"][0]["snippet"]["tags"]

    return pd.DataFrame([response_dict])

def data_source_transscripts(video_id):
    return pd.DataFrame(YouTubeTranscriptApi.get_transcript(video_id))

def video_id_collector(url):
    return url.split("v=")[1].split("&t=")[0]


videoId = "Y4GVkBWX0R4"
df1 = data_source_transscripts(videoId)
df2 = data_source(videoId)

df1.to_csv("test2.csv")
df2.to_csv("test.csv")

url = "https://www.youtube.com/watch?v=-yzfxeMBe1s"

print(video_id_collector(url))
#
# todo sentiment Analyse
# todo Big five einlesen

# todo Machine learning (advanced) - kommt später
# todo Daten ordentlich abspeichern (Nächster Schritt: In MangoDb ordentlich speichern - Später!)
# todo pentagon Diagram

