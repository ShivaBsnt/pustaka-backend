📚 Pustaka Backend – SSO Service

Pustaka Backend is a Django-based RESTful API that functions as the Single Sign-On (SSO) authentication service for the Pustaka platform. It centralizes user authentication, enabling seamless and secure access across various Pustaka services.

🔐 Key Features
* Centralized Authentication: Provides a unified login system for all Pustaka applications.

* OAuth 2.0 Support: Implements OAuth 2.0 protocols for secure and standardized authentication.

* User Management: Handles user registration, profile management, and authentication flows.

* Token-Based Access: Issues and manages access tokens for client applications.

🛠️ Technologies Used

* Framework: Django

* Language: Python

* Authentication: OAuth 2.0

* Database: SQLite (default; configurable to PostgreSQL or MySQL)


📂 Project Structure
```console
pustaka-backend/
├── client/             # Frontend client (if applicable)
├── licenses/           # License management module
├── oauth/              # OAuth authentication module
├── pustaka/            # Core application logic
├── user/               # User management module
├── manage.py           # Django's command-line utility
├── .gitignore          # Git ignore file
```
⚙️ Installation & Setup

1. Clone the repository:

```console
git clone https://github.com/ShivaBsnt/pustaka-backend.git
cd pustaka-backend
```
2. Create a virtual environment:

```console
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```console
pip install -r requirements.txt
```
4. Apply migrations:
```console
python manage.py migrate
```
5. Run the development server:
```console
python manage.py runserver
```

🤝 Contributing
Contributions are welcome! Please follow these steps:
1.Fork the repository.
2. Create a new branch:

```console 
git checkout -b feature/YourFeatureName
```
3. Commit your changes:
```console
git commit -m "Add your message here" 
```
4. Push to the branch:
```console
git push origin feature/YourFeatureName
```
5. Open a Pull Request.

📜 License
This project is dual-licensed:

Code: MIT License – Permits reuse, modification, and distribution of the software.

Documentation: Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0) – Allows others to remix, tweak, and build upon the work non-commercially, as long as they credit the author.

For more details, refer to the [LICENSE](https://github.com/ShivaBsnt/pustaka-backend/tree/master/licenses) file.

📬 Contact
For any inquiries or feedback, please email me at [shivabahadurbasnet313@gmail.com](mailto:shivabahadurbasnet313@gmail.com).