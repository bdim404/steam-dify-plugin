# Steam Dify Plugin

A Dify plugin for integrating Steam Web API functionality to query player information, game statistics, friend lists, and other Steam-related data.

## About Steam

Steam is one of the largest digital game distribution platforms in the world, developed by Valve Corporation. It serves not only as a game store but also provides community features, player profiles, achievement systems, and game statistics. The Steam Web API allows developers to access this data, providing users with a richer gaming experience and data analysis capabilities.

You can visit the [Steam official website](https://store.steampowered.com/) for more information.

## Usage

### Install

You can download [the latest release](https://github.com/bdim404/steam/releases/latest) and upload it to the Dify platform. For detailed instructions, please refer to [Install and Use Plugins: Local File Upload](https://docs.dify.ai/plugins/quick-start/install-plugins#local-file-upload).

### Packing (Optional)

If you want to pack this plugin yourself, make sure you have [dify-plugin-daemon](https://github.com/langgenius/dify-plugin-daemon/releases) installed, and then download or `git clone` this repository. After that, you can pack it using the following command:

```
dify-plugin-daemon plugin package ./steam
```

For more information, please refer to [Tool Plugin: Packing Plugin](https://docs.dify.ai/plugins/quick-start/develop-plugins/tool-plugin#packing-plugin).

### Set Up Authorization

After installing the plugin, you need to configure the connection to the Steam Web API.

You need to provide the following credentials:

- **API Key**: Authorization key for accessing the Steam Web API
- **Steam ID**: Your 17-digit Steam ID (for API key validation)

You can apply for and obtain an API Key from the [Steam Developer website](https://steamcommunity.com/dev/apikey). You need to have a valid Steam account and agree to the Steam Web API Terms of Use.

During the setup process, the plugin will verify your credentials to ensure that it can successfully connect to the Steam API service.

Once the authorization setup is complete, you can interact with the Steam API using this plugin.

### Features

This plugin supports the following features:

1. **Player Information Query**: Query basic profile information for Steam users, including username, avatar, profile URL, and online status.

2. **Game News Retrieval**: Get the latest news and update announcements for specific games.

3. **Global Game Achievement Statistics**: Query global achievement completion rate statistics for games.

4. **Detailed Player Profiles**: Get detailed player profile information, including real name (if public), account creation time, location information, etc.

5. **Friend List Query**: Get a player's Steam friend list, including when friends were added and relationship type.

6. **Player Game Achievements**: Query a player's unlocked achievements in specific games and their unlock times.

7. **Game Statistics Data**: Get detailed player statistics in specific games, such as playtime, score, kill count, and other game-specific metrics.

8. **Owned Games List**: Get a list of all games owned by a player, including playtime statistics and game icons.

9. **Recently Played Games**: Query the list of games a player has played in the last two weeks and their playtime.

You can call this plugin in Dify workflows or elsewhere. All parameters have detailed annotations. Simply provide a Steam ID or game AppID and select the type of information you need to query to get the corresponding results.

## Use Cases

1. **Gaming Community Bots**: Create chatbots that can query player profiles, achievements, and game statistics
2. **Game Data Analysis**: Analyze player playtime, achievement completion rates, and other gaming data
3. **Game News Push**: Automatically fetch and push the latest news for specific games
4. **Player Data Dashboards**: Build personalized dashboards showing player game libraries, playtime, and achievements
5. **Friend Activity Tracking**: Monitor and display friends' recent gaming activities

## Developer Notes

When using this plugin, please note the following important information:

1. **API Usage Limits**: The Steam Web API has request rate limits. Please use it reasonably and avoid overly frequent requests
2. **Privacy Settings**: Only publicly set player profiles and game data can be accessed
3. **Compliance**: When using the Steam API, please follow the [Steam Web API Terms of Use](https://steamcommunity.com/dev/apiterms)

## Author

**Author:** bdim  
**Version:** 0.0.1  
**Type:** tool plugin