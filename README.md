# Dota 2 Finder

Finds Dota 2 Twitch streams with certain conditions:

- Must have a minimum number of users.
- Determines whether the streamer is ingame or in the main menu (using histogram analysis of the top right corner).
- Determines whether the user is using a webcam (using OpenCV Haar Cascades).
