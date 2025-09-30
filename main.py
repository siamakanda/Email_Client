import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def create_env_file():
    """Create .env file and get credentials from user input"""
    print("\n" + "🆕 .env FILE SETUP 🆕".center(50, '='))
    print("It looks like this is your first time running this script.")
    print("Let's set up your email credentials!")
    
    display_gmail_instructions()
    
    # Get credentials from user
    email = input("\nEnter your email address (e.g., your_email@gmail.com): ")
    password = input("Enter your email App Password (16 characters for Gmail): ")
    
    # Create .env file content
    env_content = f"""# Email Configuration
EMAIL_USER={email}
EMAIL_PASSWORD={password}
"""
    
    # Write to .env file
    try:
        with open('.env', 'w') as env_file:
            env_file.write(env_content)
        print("✅ .env file created successfully!")
        print("🔒 Your credentials have been saved securely in the .env file")
        
        # Reload environment variables
        load_dotenv()
        return True
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def check_and_setup_env():
    """Check if .env exists and set it up if needed"""
    if not os.path.exists('.env'):
        print("📁 .env file not found...")
        return create_env_file()
    
    # Load existing .env file
    load_dotenv()
    
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')
    
    # Check if credentials are set
    if not from_email or not password:
        print("⚠️  .env file exists but credentials are missing or incomplete...")
        return create_env_file()
    
    # Check if credentials look valid
    if from_email == "your_email@gmail.com" or password == "your_app_password":
        print("⚠️  Default credentials detected in .env file...")
        return create_env_file()
    
    return True

def display_welcome_message():
    """Display a welcome message when the script starts"""
    print("🎉 Welcome to Simple Email Sender! 🎉")
    
    # Check and setup environment
    if not check_and_setup_env():
        print("❌ Failed to set up environment. Please try again.")
        return False
    
    print("✅ Credentials setup is complete!")
    print("You're ready to send emails!")
    print("-" * 50)
    return True

def send_email(to_email, subject, message):
    """Send an email using credentials from .env file"""
    # Get credentials from .env file
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')
    
    # Double-check credentials
    if not from_email or not password:
        print("❌ Error: Email credentials not found")
        if check_and_setup_env():
            # Retry with new credentials
            from_email = os.getenv('EMAIL_USER')
            password = os.getenv('EMAIL_PASSWORD')
        else:
            return False
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Add message body
    msg.attach(MIMEText(message, 'plain'))
    
    # Send email
    try:
        print(f"📧 Sending email from: {from_email}")
        print(f"📧 To: {to_email}")
        print(f"📝 Subject: {subject}")
        print("⏳ Sending...")
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        
        print("✅ Email sent successfully!")
        print("-" * 50)
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed!")
        print("💡 This usually means:")
        print("   - You're using your regular password instead of an App Password")
        print("   - Your App Password is incorrect")
        print("   - 2-factor authentication is not enabled")
        print("\nLet's update your credentials...")
        
        # Recreate .env file with new credentials
        if create_env_file():
            print("🔄 Please run the script again to send your email.")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def get_email_details():
    """Get email details from user input"""
    print("\n📨 Let's compose your email!")
    to_email = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    
    print("Enter your message (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    message = "\n".join(lines)
    return to_email, subject, message

def display_gmail_instructions():
    """Display Gmail setup instructions"""
    print("\n" + "📧 GMAIL SETUP INSTRUCTIONS 📧".center(50, '='))
    print("For Gmail, you need to:")
    print("1. Enable 2-factor authentication")
    print("2. Generate an App Password:")
    print("   • Go to Google Account → Security → 2-Step Verification")
    print("   • Click on 'App passwords'")
    print("   • Generate password for 'Mail'")
    print("   • Use the 16-character password (not your regular password)")
    print("=" * 50)

def main():
    """Main function"""
    # Display welcome and setup environment
    if not display_welcome_message():
        return
    
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Send an email")
        print("2. Update email credentials")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Get email details and send
            to_email, subject, message = get_email_details()
            
            if to_email and subject and message:
                send_email(to_email, subject, message)
            else:
                print("❌ Please fill in all email details.")
                
        elif choice == '2':
            # Update credentials
            print("\nUpdating email credentials...")
            if create_env_file():
                print("✅ Credentials updated successfully!")
            else:
                print("❌ Failed to update credentials.")
                
        elif choice == '3':
            print("\n👋 Thank you for using Simple Email Sender! Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# Run the script
if __name__ == "__main__":
    main()