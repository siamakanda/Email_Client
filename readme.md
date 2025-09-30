# 📧 Simple Email Sender

A user-friendly Python script that allows you to send emails directly from your terminal with an interactive setup and secure credential management.

## ✨ Features

- **🔐 Secure Credential Storage** - Uses `.env` file to store email credentials
- **🔄 Interactive Setup** - Guides you through initial setup if no configuration exists
- **📝 Easy-to-Use Menu** - Simple text-based interface for sending emails
- **📧 Multi-line Messages** - Support for composing multi-line email content
- **🛡️ Gmail App Password Support** - Works with Gmail's secure App Passwords
- **♻️ Credential Management** - Easy option to update credentials if needed

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- A Gmail account (or other email provider with SMTP support)
- 2-factor authentication enabled (for Gmail)

### Installation

1. **Save the script as `main.py`**

2. **Install required dependencies:**
   ```bash
   pip install python-dotenv
   ```

3. **Run the script:**
   ```bash
   python main.py
   ```

## 📋 First-Time Setup

When you run the script for the first time, it will automatically guide you through the setup process:

1. **The script detects no `.env` file** and starts the setup wizard
2. **You'll see Gmail setup instructions** with step-by-step guidance
3. **Enter your credentials:**
   - Your email address (e.g., `your_email@gmail.com`)
   - Your App Password (16-character password for Gmail)

4. **The script creates a `.env` file** with your secure credentials

### 🔧 Gmail App Password Setup

For Gmail users, you need to generate an App Password:

1. **Enable 2-Factor Authentication:**
   - Go to [Google Account](https://myaccount.google.com)
   - Navigate to Security → 2-Step Verification → Turn on

2. **Generate App Password:**
   - Go to Security → 2-Step Verification → App passwords
   - Select "Mail" as the app and "Other" as the device
   - Enter "Python Email Sender" as the name
   - Copy the 16-character password shown

3. **Use the App Password** in the script setup (not your regular Gmail password)

## 🎮 How to Use

### Main Menu Options

After setup, you'll see the main menu:

```
What would you like to do?
1. Send an email
2. Update email credentials
3. Exit
```

#### Option 1: Send an Email
- Enter recipient's email address
- Enter email subject
- Compose your message (press Enter twice to finish)
- The script sends the email and shows success/failure status

#### Option 2: Update Email Credentials
- Re-run the setup wizard to update your email and password
- Useful if you change passwords or want to use a different account

#### Option 3: Exit
- Close the application

## 🛠️ Technical Details

### File Structure
```
project/
├── main.py          # Main Python script (your file)
├── .env             # Auto-created credential file (ignored by git)
└── README.md        # This file
```

### Environment Variables
The `.env` file contains:
```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

### Security Notes
- 🔒 Credentials are stored locally in `.env` file
- 🚫 The `.env` file should be added to `.gitignore` if using version control
- 🔑 Uses App Passwords instead of regular passwords for Gmail
- 📧 Emails are sent over encrypted TLS connection

## ❓ Troubleshooting

### Common Issues

**Authentication Failed Error:**
- Ensure you're using an App Password, not your regular password
- Verify 2-factor authentication is enabled
- Check that the App Password was generated for "Mail"

**SMTP Connection Errors:**
- Check your internet connection
- Verify SMTP settings for your email provider
- For non-Gmail providers, you may need to adjust SMTP server settings

**Script Can't Create .env File:**
- Ensure you have write permissions in the script directory
- Check if a `.env` file already exists and is read-only

### Supported Email Providers

- **Gmail** (recommended) - Uses `smtp.gmail.com:587`
- **Outlook/Hotmail** - Use `smtp-mail.outlook.com:587`
- **Yahoo** - Use `smtp.mail.yahoo.com:587`
- Other providers with SMTP support (modify SMTP settings in code)

## 🔄 Updating the Script

To use with other email providers, modify the SMTP settings in the `send_email` function in `main.py`:

```python
# Change this line for different providers
server = smtplib.SMTP('smtp.gmail.com', 587)
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## ⚠️ Disclaimer

This tool is for personal and educational use. Always comply with your email provider's terms of service and anti-spam policies.

---

**Happy Email Sending!** 📨✨