from services.chat_service import ChatService

# TODO: Initialize a ChatService instance
chat_service = ChatService()

# TODO: Define a variable with a sample user identifier, e.g., "user123"
user_id = "user1234"

# TODO: Call the create_chat method with the user ID and store the chat ID
chat_id = chat_service.create_chat(user_id)

# TODO: Print the chat ID
print(f"chat session created with ID: {chat_id}")