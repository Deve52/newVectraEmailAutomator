# Vectra Email Automator

A web-based platform designed to simplify bulk email communication while providing a collaborative space to improve email engagement strategies.

## Overview

Vectra Email Automator is a dual-purpose system that combines email automation with a community discussion platform. It helps users send bulk emails efficiently and learn better engagement techniques through shared knowledge.

The project addresses the growing rise of spam and declining email engagement by focusing on office workers who still depend on email communication, providing efficient bulk scheduling and sending tools, and creating a collaborative forum where users can exchange strategies to improve content quality and boost engagement.

## Features of This Project

### Email Automation

- Bulk email sending to multiple recipients
- Email scheduling and recurring campaigns
- Contact grouping and segmentation
- CSV import for managing recipient lists
- Email templates and personalization

### Contact Management

- Create and manage organizations
- Group-based email management
- Easy add/edit/delete contacts

### Dashboard

- Overview of campaigns and schedules
- Email history tracking
- Organization and group insights

### Community Platform

- Discussion threads on email strategies
- User interaction via replies and topics
- Knowledge sharing and problem-solving

### Authentication & Security

- User registration and login system
- Secure password handling
- Session-based authentication

## Tech Stack

### Backend

- Django 5.2.8
- Python

### Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

### Database

- SQLite (development)
- Scalable to PostgreSQL/MySQL (production)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/areeb-x3/vectra-email-automator.git
cd vectra-email-automator
```


### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Server

```bash
python manage.py runserver
```

## Documentation

For Installing, Deploying and Building the App reffer to [Docs](/docs)