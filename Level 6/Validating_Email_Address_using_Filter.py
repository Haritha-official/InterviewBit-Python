def valid_email(email: str) -> bool:
    """
    Validate an email address based on simple rules:
    - Must contain '@'
    - Username can contain only alphanumeric characters, hyphens (-), or underscores (_)
    - Website (domain) must be alphanumeric
    - Extension must be alphabetic and up to 3 characters long
    """
    
    # Check for presence of '@'
    if "@" not in email:
        return False
        
    try:
        # Split into username and domain part
        username, rest = email.split("@")
        
        # Further split domain into website and extension
        website, extension = rest.split(".")
    except ValueError:
        # If splitting fails, structure is invalid
        return False
        
    # Validate username (only alphanumeric, '-' or '_')
    if not all(c.isalnum() or c in "-_" for c in username):
        return False
        
    # Website (domain) must be alphanumeric
    if not website.isalnum():
        return False
        
    # Extension must be alphabetic and max 3 letters (like com, org, net)
    if not (extension.isalpha() and len(extension) <= 3):
        return False
        
    return True
    
    
def main():
    """
    Main driver function:
    - Takes N (number of emails) as input
    - Reads N emails from user
    - Filters only valid emails using valid_email()
    - Sorts and prints the valid emails
    """
    
    # Number of emails
    N = int(input())
    
    # Read all emails
    emails = [input().strip() for _ in range(N)]
    
    # Keep only valid emails
    valid_emails = list(filter(valid_email, emails))
    
    # Sort lexicographically
    valid_emails.sort()
    
    # Print result
    print(valid_emails)
    
    
# Program entry point
if __name__ == "__main__":
    main()
