# Deploying

This guide covers the basic steps required to deploy the project on a production machine.

## 1. Clone the Repository

Clone the project from GitHub and navigate into the directory:

```bash
git clone https://github.com/areeb-x3/vectra-email-automator.git
cd vectra-email-automator
```

## 2. Create a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
python -m venv venv
```

Activate the environment:

* **Linux / macOS**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This includes Django and required third-party libraries such as `google-auth`.

## 4. Apply Migrations

Apply database migrations to set up the database schema:

```bash
python manage.py migrate
```

## 5. Select Database

Choose a database based on your production requirements. By default, Django uses SQLite, which is suitable for development and small projects. For production, it is recommended to use a more robust relational database system such as PostgreSQL.

You can configure the database in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

To use a different database (e.g., PostgreSQL), update the `ENGINE` and provide the required connection details.

```python
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'your_database_name', 
        'USER': 'your_database_user', 
        'PASSWORD': 'your_password', 
        'HOST': 'localhost', 
    } 
}
```

## 6. Get Google Cloud Credentials

To enable Google API access (e.g., Gmail), you need to create OAuth 2.0 credentials from Google Cloud.

### 1. Create a Project

* Go to the Google Cloud Console
* Click **Select Project → New Project**
* Enter a name and create the project

---

### 2. Enable Required APIs

* Navigate to **APIs & Services → Library**
* Enable the required APIs (e.g., Gmail API)

---

### 3. Configure OAuth Consent Screen

* Go to **APIs & Services → OAuth consent screen**
* Choose **External**
* Fill in required details:

  * App name
  * Support email
  * Authorized domains (your production domain)
* Save and continue

---

### 4. Create OAuth Credentials

* Go to **APIs & Services → Credentials**
* Click **Create Credentials → OAuth Client ID**
* Select **Web Application**
* Add:

  * **Authorized Redirect URIs** (e.g., `http://localhost:8000/callback/` for development or your production domain)

---

### 5. Download Credentials

* After creation, download the credentials JSON file
* Place it securely in your project (e.g., `credentials.json`)

---

## 7. Start Server

### Local Development

To start the development server locally:

```bash
python manage.py runserver
```

By default, the server runs at `http://127.0.0.1:8000/`. You can also specify a custom host and port:

```bash
python manage.py runserver 127.0.0.4:5600
```

To make the server accessible on your local network, run at `http://127.0.0.1:<port>/`. You can then access it using your machine’s IP address: `http://<your-local-ip>:<port>/`

> [!NOTE]
> Google Cloud does not allow OAuth authentication requests from private or local IP addresses (e.g., `192.168.x.x`) in production.
>
> To enable authentication, you must use a public domain and configure it in your Google Cloud Console:
>
> * Add your domain to **Authorized Domains**
> * Configure the **OAuth Consent Screen**
> * Add your domain to **Authorized Redirect URIs**
>
> Without this configuration, authentication requests will be blocked.

### Production Setup (Custom Domain)

The built-in Django development server is **not suitable for production**. For deploying with a custom domain:

1. **Use a production server** such as:

   * Gunicorn (WSGI server)
   * Uvicorn (ASGI server)

2. **Run the application using Gunicorn:**

```bash
pip install gunicorn
gunicorn your_project_name.wsgi:application
```

3. **Set up a reverse proxy (Nginx):**

   * Point your domain (e.g., `example.com`) to your server’s IP
   * Configure Nginx to forward requests to Gunicorn

4. **Update Django settings:**

```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
DEBUG = False
```
