import praw  # type: ignore # Import the Reddit API library
import requests  # type: ignore # Import the requests library to interact with the Groq AI API
import schedule  # type: ignore # Import the scheduling library to schedule daily posts
import time  # Import time to delay the script between runs
import logging  # Import logging to capture errors and actions

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Reddit API credentials
REDDIT_CLIENT_ID = 'your_client_id'  # Your Reddit client ID
REDDIT_SECRET = 'your_client_secret'  # Your Reddit client secret
REDDIT_USER_AGENT = 'your_user_agent'  # Your Reddit user agent
REDDIT_USERNAME = 'your_username'  # Your Reddit username
REDDIT_PASSWORD = 'your_password'  # Your Reddit password

# Groq API credentials
GROQ_API_URL = 'https://api.groq.ai/generate'  # Groq API URL
GROQ_API_KEY = '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'  # Your Groq API key

# Initialize Reddit API client
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT, username=REDDIT_USERNAME,
                     password=REDDIT_PASSWORD)

# Function to generate content using Groq AI
def generate_content():
    try:
        headers = {'Authorization': f'Bearer {GROQ_API_KEY}'}  # Set the API authorization header
        data = {'prompt': 'Generate a random interesting Reddit post.', 'max_tokens': 100}  # Groq request data
        response = requests.post(GROQ_API_URL, headers=headers, json=data)  # Send the request to Groq API
        response.raise_for_status()  # Raise an error for invalid responses

        # Return the generated content if successful
        return response.json()['text']
    except requests.exceptions.RequestException as e:
        logging.error(f"Error generating content: {e}")  # Log any API request errors
        return None

# Function to post content to Reddit
def post_content():
    content = generate_content()  # Generate content using the Groq API
    if content:
        try:
            subreddit = reddit.subreddit('your_subreddit')  # Specify the subreddit to post in
            subreddit.submit('Generated Content', selftext=content)  # Post the content to Reddit
            logging.info("Content posted successfully!")  # Log the success
        except Exception as e:
            logging.error(f"Error posting content: {e}")  # Log any posting errors

# Function to schedule daily posts at the user-specified time
def schedule_posts():
    post_time = '09:00'  # Specify the time for posting (24-hour format)
    schedule.every().day.at(post_time).do(post_content)  # Schedule the post content function

    # Run the scheduled posts indefinitely
    while True:
        schedule.run_pending()  # Run any scheduled tasks
        time.sleep(60)  # Wait a minute before checking again

# Main function to start the bot
if __name__ == "__main__":
    logging.info("Reddit bot started.")  # Log the bot startup
    schedule_posts()  # Start the scheduling system
