# PlayStation 5 E-commerce Website
Welcome to the development journey of our PlayStation 5 e-commerce website. This project aims to provide a seamless and efficient shopping experience for PlayStation 5 enthusiasts.

## About the Project

This monorepo project contains multiple frontend applications and a backend server for the PS5 Store application. The frontend is developed using React, and the backend is developed using Flask (Python). This setup uses Yarn Workspaces for managing dependencies and scripts.

## Project Structure

```txt
  /ps5-store
    /frontend # Frontend Development
      ...
    /backend # Backend Development
      ...
```

## Key Takeaways
- Combining React and Flask for an easier e-commerce experience
- Emphasis on sleek design and functionality
- Robust backend to ensure data safety and efficient order processing
- Best practices to enhance user experience and ensure success
- Continuous improvement driven by user feedback and performance monitoring

## Sleek Design Meets Functionality
We intended to have the website look stylish with easy-to-use functionalities. Users surfing it comfortably can browse through PlayStation 5 consoles, games, and accessories.

### Components of Design
- Lists consoles, games, and accessories with images
- User-friendly interface ensuring smooth navigation

## Robust Backend with Flask
In the backend, we are using Flask, which is a simple and powerful web framework. It handles user login, order processing, and maintaining data safety efficiently.

### Backend Features
- Shopping cart and purchase are swiftly processed
- Protection of the information of customers and details of their transactions

## Best Practices for E-commerce Success
- Easy navigation and search so users can find what they want quickly
- Simple and fast checkout process
- Mobile-friendly design ensuring the site works well on all devices

## Continuous Improvement
We are always looking for ways to make our site better. User feedback and continuous site monitoring are integral in making value-based decisions aimed at improving the site further.

### Performance Monitoring Tools
- Assists in observing user actions on the website and its performance
- Gathers opinions and suggestions from users


## Unique Features
- Put a great search functionality via keywords, categories, and filters
- Users can filter their search results with the help of price ranges, varying from ratings to even product types, something essential for users who are always on the go
- End of a guessing game—this helps users find what they want faster

## Developer Guide

### Technologies Used

**Frontend:**
- Bootstrap
- Framer Motion
- React
- React Paginate
- React Redux
- React Slick
- React Toastify
- Redux Persist
- Slick Carousel
- Tailwind Scrollbar

**Backend:**
- Flask
- Swagger
- Authentications Package using JWT (Custom Made Package)
- SQLite for development based database
- MySQL for Production based database
- Unittesting
- SQLAlchemy
- Permission & Validator packages (Custom Made Package)
- Serializers (Custom Made Package)
- Pydantic

## Prerequisites

- Node.js and Yarn
- Python and pip

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ps5-store.git
   cd ps5-store
   ```

2. **Install the dependencies:**

   ```bash
   yarn install
   ```

3. **Install Python dependencies for the backend:**

   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

## Scripts

The following scripts are available to manage the different projects in the monorepo:

- **Start Admin Login Frontend:**

  ```bash
  yarn start:admin_login
  ```

- **Start Management Frontend:**

  ```bash
  yarn start:managment
  ```

- **Start Staff Frontend:**

  ```bash
  yarn start:staff
  ```

- **Start Store Frontend:**

  ```bash
  yarn start:store
  ```

- **Start Backend:**

  ```bash
  yarn start:backend
  ```

- **Start All (Frontend and Backend):**

  ```bash
  yarn start:all
  ```

## Running the Project

To start both the Flask backend and the React frontend (Store), run the following command from the root of the project:

```bash
yarn start:all
```

This command uses `concurrently` to start both the backend and the frontend servers simultaneously. The backend will run on port 5000 by default, and the frontend will run on port 3000 by default.

## Frontend (React)

The React frontend handles the user interface and makes API calls to the backend.

### Example API Call

In your React components, you can make API calls to the backend like this:

```jsx
import axios from 'axios';

const handleLogin = async () => {
  try {
    const response = await axios.post('http://localhost:5000/login', {
      username,
      password,
    });
    localStorage.setItem('token', response.data.access_token);
    window.location.href = '/management';
  } catch (error) {
    console.error('Error logging in', error);
  }
};
```

## Acknowledgements

- **Company:** [AlX-SE Africa Software Engineering Company](https://www.alxafrica.com/)
- **Frontend Developer:** Zerihun Shiferaw ([Zed-bard](https://github.com/Zed-bard))
- **Backend Developer:** Waheed Khaled ([Wehda23](https://github.com/Wehda23))

### Community

- [React](https://reactjs.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Yarn Workspaces](https://classic.yarnpkg.com/en/docs/workspaces/)
- [Concurrently](https://www.npmjs.com/package/concurrently)
