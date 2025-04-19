from bs4 import BeautifulSoup
import csv

def scrape_album(album):

    # Extract the title
    title_div = album.find(class_="page_charts_section_charts_item_title")
    title = title_div.find(class_="ui_name_locale_original").text.strip()

    # Extract the artist
    artist_div = album.find(class_="artist")
    artist = artist_div.text.replace("\n", "").strip() if artist_div else ""

    # Extract the date
    date_div = album.find(class_="page_charts_section_charts_item_date")
    date = date_div.find("span").text.replace("\n", "").strip() if date_div else ""

    # Extract the primary genres
    primary_div = album.find(class_="page_charts_section_charts_item_genres_primary")
    primary = primary_div.text.strip().replace("\n", ", ") if primary_div else ""

    # Extract the secondary genres
    secondary_div = album.find(class_="page_charts_section_charts_item_genres_secondary")
    secondary = secondary_div.text.strip().replace("\n", ", ") if secondary_div else ""

    # Extract the score (average rating)
    score_div= album.find(class_="page_charts_section_charts_item_details_average_num")
    score = score_div.text.strip() if score_div else ""

    # Extract the number of ratings 
    ratings_div = album.find(class_="page_charts_section_charts_item_details_ratings")
    ratings_text = ratings_div.text.replace("\n", "").replace("/", "").strip()
    ratings = ratings_text.replace("k", "000")

    # Extract the number of reviews
    reviews_div = album.find(class_="page_charts_section_charts_item_details_reviews")
    reviews_text = reviews_div.text.replace("\n", "").replace("/", "").strip()
    reviews = reviews_text.replace("k", "000")

    # Return the extracted data
    return [title, artist, date, primary, secondary, score, ratings, reviews]


def scrape_album_page(page):

    # Open and read the saved HTML
    with open(f"pages/albums/{page}.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    albums = soup.find_all(class_="page_charts_section_charts_item")

    # Get all albums from the page
    page_data = []
    for i, album in enumerate(albums):
        rank = (i + 1) + (40 * int(page))
        data = scrape_album(album)
        page_data.append([rank] + data)

    return page_data


def get_album_data():

    # Iterate through all pages
    album_data = []
    for i in range(126):
        print(f"Scraping album page {i}")
        page = str(i).zfill(3)
        page_data = scrape_album_page(page)
        album_data += page_data

    # Save the album data to a CSV file
    with open('data/albums.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(album_data)


def scrape_song(song):

    # Extract the title
    title_div = song.find(class_="page_charts_section_charts_item_title")
    title = title_div.find(class_="ui_name_locale_original").text.strip()

    # Extract the artist
    artist_div = song.find(class_="artist")
    artist = artist_div.text.replace("\n", "").strip() if artist_div else ""

    # Extract the date
    date_div = song.find(class_="page_charts_section_charts_item_date")
    date = date_div.find("span").text.replace("\n", "").strip() if date_div else ""

    # Extract the primary genres
    genre_div = song.find(class_="page_charts_section_charts_item_genres_primary")
    genre = genre_div.text.strip().replace("\n", ", ") if genre_div else ""

    # Extract the score (average rating)
    score_div= song.find(class_="page_charts_section_charts_item_details_average_num")
    score = score_div.text.strip() if score_div else ""

    # Extract the number of ratings 
    ratings_div = song.find(class_="page_charts_section_charts_item_details_ratings")
    ratings_text = ratings_div.text.replace("\n", "").replace("/", "").strip()
    ratings = ratings_text.replace("k", "000")

    # Return the extracted data
    return [title, artist, date, genre, score, ratings]


def scrape_song_page(page):

    # Open and read the saved HTML
    with open(f"pages/songs/{page}.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    songs = soup.find_all(class_="page_charts_section_charts_item")

    # Get all songs from the page
    page_data = []
    for i, song in enumerate(songs):
        rank = (i + 1) + (40 * int(page))
        data = scrape_song(song)
        page_data.append([rank] + data)

    return page_data


def get_song_data():

    # Iterate through all pages
    song_data = []
    for i in range(126):
        print(f"Scraping song page {i}")
        page = str(i).zfill(3)
        page_data = scrape_song_page(page)
        song_data += page_data

    # Save the song data to a CSV file
    with open('data/songs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(song_data)


# Run the scrapers on the saved album pages and song pages
get_album_data()
get_song_data()
