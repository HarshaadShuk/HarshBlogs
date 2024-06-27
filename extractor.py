def extract_title_and_content(file_path):
    # Initialize variables to store title and content
    title = None
    content = ""

    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            file_content = file.read()
            
            # Extract title (assuming it's within { } after "Heading = ")
            start_title_index = file_content.find("Heading = {")
            if start_title_index != -1:
                end_title_index = file_content.find("}", start_title_index)
                if end_title_index != -1:
                    title = file_content[start_title_index + len("Heading = {"):end_title_index].strip()

            # Extract content (assuming it's within { } after "BODY = ")
            start_body_index = file_content.find("BODY = {")
            if start_body_index != -1:
                end_body_index = file_content.find("}", start_body_index)
                if end_body_index != -1:
                    content = file_content[start_body_index + len("BODY = {"):end_body_index].strip()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None, None
    
    # Return title and content
    return title, content

# # Example usage:
# file_path = 'example.txt'  # Replace with your file path
# title, content = extract_title_and_content(file_path)

# if title and content:
#     print(f"Title: {title}")
#     print(f"Content:")
#     print(content)
