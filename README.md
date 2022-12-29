# Discord Combo Maker Bot

This Discord bot is a tool for generating and downloading combo lists. It can be invoked using the `?make` command, and will scrape a specified website for combo lists and download a specified number of them. The combo lists are then sent to the user through Discord.

The bot also has a `?ping` command that returns the connection speed in milliseconds, and a `?helpp` command that provides a list of available commands and their descriptions. Additionally, there is a `?upgradetool` command that sends a message with a link to a tool for upgrading combo lists.

The `on_ready` event is triggered when the bot is logged in and ready to start receiving commands, and the `on_message` event is triggered whenever a message is sent in a Discord channel that the bot has access to. These events, along with several utility functions, help to provide a useful and functional tool for generating and downloading combo lists in Discord.
