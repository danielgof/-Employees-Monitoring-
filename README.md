# Employees Monitoring

Employees Monitoring is a full-stack application designed to monitor and manage employee activities and performance. This application leverages React and TypeScript for the client-side and Flask with PostgreSQL and Redis for the backend. The entire application is containerized using Docker and Docker Compose.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication: Secure login and registration system.
- Employee Management: Add, update, and remove employee details.
- Activity Tracking: Monitor employee activities and performance.
- Real-Time Notifications: Instant updates on important events.
- Dashboard: Visual representation of employee metrics and data.
- Reporting: Generate and export performance reports.

## Technologies Used

### Frontend

- **React**: A JavaScript library for building user interfaces.
- **TypeScript**: A typed superset of JavaScript that compiles to plain JavaScript.

### Backend

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: An ORM for database interactions.
- **PostgreSQL**: The database system.
- **Redis**: For caching and message brokering.

### Containerization

- **Docker**: For containerizing the application.
- **Docker Compose**: For orchestrating multi-container Docker applications.

## Architecture

The application is designed using a microservices architecture. The backend consists of multiple Flask services, each responsible for different aspects of the application, such as user management, activity tracking, and reporting. The frontend is a React application that communicates with these microservices through RESTful APIs.

### High-Level Diagram

```
+-------------+      +------------------+      +-------------+
|   React     |<---> |  API Gateway     |<---> |   Flask      |
|   Client    |      |  (Flask)         |      |   Services   |
+-------------+      +------------------+      +-------------+
                                             /          
                                            /           
                                           /           
                                          /
                                          |
                                     +----+----+
                                     | Database |
                                     +----------+
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Node.js and npm (for frontend development)
- Python 3.8+
- PostgreSQL
- Redis

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/danielgof/Employees-Monitoring.git
    cd employees-monitoring/backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application using Docker Compose:

    ```bash
    docker-compose up --build
    ```

### Frontend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/danielgof/Employees-Monitoring.git
    cd employees-monitoring/frontend
    ```

2. Install the dependencies:

    ```bash
    npm install
    ```

3. Run the React application:

    ```bash
    npm start
    ```

## Usage

1. Register a new account or log in with existing credentials.
2. Add, update, or remove employee details.
3. Monitor employee activities and performance metrics.
4. View real-time notifications on important events.
5. Generate and export performance reports through the dashboard.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are accepted.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

