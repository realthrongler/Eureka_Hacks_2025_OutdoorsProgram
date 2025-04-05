import os
import openai

# Ensure your environment variable is correctly set
openai.api_key = os.getenv('OPENAI_API_KEY')  # This should work if the environment variable is set

if not openai.api_key:
    print("Error: API key is not set!")
    exit()  # Exit the program if the API key is not found


# Function to send a prompt to ChatGPT and get a response for generating quests
def ask_chatgpt(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" or another model if needed
            prompt=prompt,
            max_tokens=150  # Controls how much text ChatGPT will generate
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to start a countdown timer for the quest
def start_timer(quest_duration):
    print(f"You have {quest_duration} minutes to complete this quest!")
    time.sleep(quest_duration * 60)  # Wait for the specified time (in seconds)
    print("Time is up! Please submit your quest.")

# Simulate checking an image (you can replace with actual API call to Google Vision or AWS Rekognition)
def check_image(image_path, quest):
    # For the sake of simulation, we'll randomly decide if the image is correct
    correct_items = ["stop sign", "park", "local landmark"]
    if any(item.lower() in image_path.lower() for item in correct_items):
        return True
    return False

# Function to generate quests based on city
def generate_quests(city):
    prompt = f"Generate a list of items or tasks that could be found in the city of {city}. Example tasks: find a stop sign, local landmarks, etc."
    quests = ask_chatgpt(prompt)
    return quests.split('\n')  # Return tasks as a list of tasks

# Main program
def main():
    # Get user information
    username = input("Hi! Welcome to the quest app.\nWhat's your name? ")
    city = input(f"Great {username}!\nPlease input your city, province/state, and country: ")

    # Generate tasks based on the user's city
    tasks = generate_quests(city)
    print(f"Here are your tasks for today, {username}:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    # Simulate the user completing each task
    streak = 0  # Initialize the streak counter
    for i, task in enumerate(tasks, start=1):
        print(f"\nTask {i}: {task}")
        
        # Start a timer for the task (e.g., 5 minutes)
        quest_duration = 5  # minutes
        start_timer(quest_duration)

        # Ask for the image file path (or URL for submission)
        image_path = input("Please enter the path of the image you took for the task: ")

        # Check if the image matches the task (this is a simulation, replace with actual image recognition logic)
        if check_image(image_path, task):
            print(f"Good job! You completed task {i}: {task}")
            streak += 1
        else:
            print(f"Oops! The image doesn't match the task {i}: {task}. Please try again.")
            break  # End the process if the user fails a task

    # If the user completes all tasks, add to their streak
    if streak == len(tasks):
        print(f"\nCongratulations {username}! You completed all tasks and earned a streak for the day!")
        # You can store or save the streak here for tracking over time (database/file).
    else:
        print(f"\nUnfortunately, you didn't complete all tasks today, {username}. Try again tomorrow!")

if __name__ == "__main__":
    main()

