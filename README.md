<!-- Original Author - Swastik2442 (https://github.com/Swastik2442) -->
> This method doesn't work as of July 2022

# Insta-to-Discord

Send Latest Instagram Posts to Discord using Discord Webhooks

> Note: This only works for Public Accounts.

## Setup

### To run Locally
* Clone the repo using `git clone https://github.com/Swastik2442/Insta-to-Discord.git`
* Run this command from the Repo Directory `pip install -r requirements.txt --no-cache-dir`
* Add a File with name `.env` and create the following Variables-
    * `IG_USERNAME`
    * `DISCORD_WEBHOOK` <!-- https://i.imgur.com/f9XnAew.png -->

### To run Online
* Fork this Repo
* Connect your Forked Repo to the Service you are using.
* Add the following Environment Variables-
    * `IG_USERNAME`
    * `DISCORD_WEBHOOK` <!-- https://i.imgur.com/f9XnAew.png -->

### Optional Setup
The Program checks for Instagram Posts every 3 hours, this can be changed by setting time values in the [countdown()](https://github.com/Swastik2442/Insta-to-Discord/blob/main/instatodc.py#L102) function.

> ***Notes***: 
> Check this Discussion on Stack Overflow if the Method stops working - https://stackoverflow.com/q/49852080
