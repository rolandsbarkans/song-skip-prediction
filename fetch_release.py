import pandas as pd
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm

input_file = 'data/raw.csv'
output_file = 'data/raw_w_release.csv'
uri_column = 'spotify_track_uri' 

def initialize_spotify_client():
    """
    Initializes and returns a Spotipy client using environment variables.
    """
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    client = spotipy.Spotify(auth_manager=auth_manager)
    return client

def fetch_release_dates_for_uris(uris, client):
    """
    Fetches album release dates for a list of track URIs using the Spotify API.
    Returns a dictionary mapping track URI to its release date.
    """
    uri_to_date_map = {}
    batch_size = 50

    # Use tqdm for a progress bar
    for i in tqdm(range(0, len(uris), batch_size), desc="Fetching Release Dates"):
        batch = uris[i:i + batch_size]
        results = client.tracks(batch)
        for track in results['tracks']:
            if track: 
                uri_to_date_map[track['uri']] = track['album']['release_date']
            
    return uri_to_date_map

def main():
    """
    Orchestrates the data fetching and processing.
    """
    
    # Initialize the Spotify client
    sp_client = initialize_spotify_client()

    # Load merged raw data
    df = pd.read_csv(input_file, low_memory=False)
    unique_uris = df[uri_column].dropna().unique().tolist()
    print(f"Found {len(unique_uris)} unique tracks to fetch.")

    # Fetch the release date data from the Spotify API
    release_date_map = fetch_release_dates_for_uris(unique_uris, sp_client)

    # Map the release dates back to the main DataFrame
    df['release_date'] = df[uri_column].map(release_date_map)

    # Save the new information to a CSV file
    df.to_csv(output_file, index=False)

# Call the main function
if __name__ == "__main__":
    main()