# Project Overview

This repository contains two web pages designed to showcase different functionalities: a main page with a form, navigation buttons, an MP3 player, and a dynamic video showcase page using the YouTube Data API.

## Websites

### 1. Main Page (`index.html`)

The main page includes:
- **Form for File Download**: Users can input a file name and click "Submit" to download the file.
- **Navigation Buttons**: 
  - A button to go to the dynamic video showcase page.
  - A button to go to a placeholder page (`index3.html`).
- **MP3 Player**: An integrated MP3 player to play a predetermined file (`gigachad.mp3`).

#### Features

- **Form for File Download**: This form allows users to download files by entering the file name and clicking the "Submit" button.
- **Navigation Buttons**: These buttons enable navigation between different pages of the project.
- **MP3 Player**: This player can play audio files, providing basic controls like play, pause, and volume adjustment.

### 2. Dynamic Video Showcase (`index2.html`)

This page showcases a dynamic list of popular YouTube videos fetched using the YouTube Data API. It updates the videos each time the page loads.

#### Features

- **Dynamic Video Fetching**: Fetches a list of popular YouTube videos dynamically each time the page loads.
- **Back to Main Page Button**: A button to navigate back to the main page.

### How to Use

1. **View the Main Page**: Open `index.html` in your browser.
2. **Use the Form**: Enter a file name and click "Submit" to download the file.
3. **Navigate to Video Showcase**: Click the button labeled "Go to Video Showcase" to navigate to the dynamic video showcase page.
4. **View the Video Showcase**: Open `index2.html` in your browser to view a dynamic list of popular YouTube videos.
5. **Navigate Back to Main Page**: Use the "Back to Main Page" button to return to the main page from the video showcase page.

### Additional Information

- Ensure you have the required API key for fetching YouTube videos.
- The `index.html` page includes a form for downloading files and an MP3 player for playing audio files.
- The `index2.html` page dynamically loads popular YouTube videos each time the page is loaded.
