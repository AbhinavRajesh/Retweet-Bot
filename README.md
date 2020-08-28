<p align="center">
  <img height="250.0" width="250.0" src="https://miro.medium.com/max/840/1*u237xTTUp6m6JKQ14b5oGQ.png"
</p>

## Retweet-Bot
A Twitter Bot which Retweets with Comment and likes tweets with particular Hashtag

### Tech Used
- Python
- Tweepy 
- Twitter Developer API
- Visual Studio Code

### Installation
1. Get the required tokens [ API Key, Access Token Key, ... ] from [Developer Twitter](https://developer.twitter.com)
2. Clone the repository
   ```shell
   $ git clone https://github.com/AbhinavRajesh/Retweet-Bot.git
   ```
3. Navigate to Downloaded file
    ```shell
    cd Retweet-Bot
    ```
4. Make a Virtual Environment and activate it
    ```shell
    $ virtualenv env
    $ env\Scripts\activate       [For Windows]
    $(env)
    ```
5. Install required Dependencies
    ```shell
    $(env) pip install tweepy
    ```
6. Edit the values of the variables with the tokens which you got from Developer Twitter API
    ``` 
    Check the comments inside the twitter.py file to know where to add the values
    ```
7. Run the App!
    ```shell 
    $(env) py twitter.py
    ```
    
### Issues
Currently there is one bug which I'm aware of and I'm also working on the same and would be resolved in future.
