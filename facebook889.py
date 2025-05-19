import facebook
import time
import json
import requests
from getpass import getpass

def delete_all_messages():
    """
    Delete all messages from Facebook Messenger using the Graph API
    This requires a valid access token with appropriate permissions
    """
    print("Facebook Messenger Message Deletion Tool")
    print("---------------------------------------")
    
    # Get access token - in production, use a more secure method
    access_token = getpass("Enter your Facebook Graph API access token: ")
    
    # Initialize the Graph API client
    graph = facebook.GraphAPI(access_token)
    
    try:
        # Get user info to verify the token works
        user = graph.get_object("me")
        print(f"Authenticated as: {user['name']}")
        
        # Get conversations (threads)
        conversations = graph.get_connections("me", "conversations", limit=100)
        
        if not conversations['data']:
            print("No conversations found.")
            return
            
        print(f"Found {len(conversations['data'])} conversations.")
        
        # Process each conversation
        for conversation in conversations['data']:
            conversation_id = conversation['id']
            
            # Get basic info about the conversation
            convo_info = graph.get_object(conversation_id)
            
            if 'name' in convo_info:
                convo_name = convo_info['name']
            else:
                # For direct messages without names
                participants = graph.get_connections(conversation_id, "participants")
                participant_names = [p.get('name', 'Unknown') for p in participants['data'] if p['id'] != user['id']]
                convo_name = ", ".join(participant_names) if participant_names else "Unknown conversation"
            
            print(f"\nProcessing conversation: {convo_name}")
            
            # Get messages in this conversation
            messages = graph.get_connections(conversation_id, "messages", limit=100)
            
            if not messages['data']:
                print("  No messages found in this conversation.")
                continue
                
            print(f"  Found {len(messages['data'])} messages. Deleting...")
            
            # Delete each message the user sent
            deleted_count = 0
            for message in messages['data']:
                # Only delete messages sent by the user
                if message.get('from', {}).get('id') == user['id']:
                    try:
                        # Delete the message
                        graph.delete_object(message['id'])
                        deleted_count += 1
                        print(f"  Deleted message: {message['id']}")
                        # Add a small delay to avoid rate limiting
                        time.sleep(0.5)
                    except facebook.GraphAPIError as e:
                        print(f"  Error deleting message {message['id']}: {str(e)}")
            
            print(f"  Deleted {deleted_count} messages in this conversation.")
            
            # Process pagination to get more messages if available
            while 'paging' in messages and 'next' in messages['paging']:
                try:
                    # Get the next page URL from the paging info
                    next_url = messages['paging']['next']
                    response = requests.get(next_url)
                    messages = response.json()
                    
                    if not messages['data']:
                        break
                        
                    print(f"  Found {len(messages['data'])} more messages. Deleting...")
                    
                    # Delete each message
                    for message in messages['data']:
                        if message.get('from', {}).get('id') == user['id']:
                            try:
                                graph.delete_object(message['id'])
                                deleted_count += 1
                                print(f"  Deleted message: {message['id']}")
                                time.sleep(0.5)
                            except facebook.GraphAPIError as e:
                                print(f"  Error deleting message {message['id']}: {str(e)}")
                                
                except Exception as e:
                    print(f"  Error processing next page: {str(e)}")
                    break
            
            print(f"  Total deleted in conversation: {deleted_count} messages")
        
        print("\nMessage deletion process completed.")
        
    except facebook.GraphAPIError as e:
        print(f"Facebook API Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    delete_all_messages()