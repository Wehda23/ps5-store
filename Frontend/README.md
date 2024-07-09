# PlayStation 5 E-commerce Frontend Development
Welcome to the development journey of our PlayStation 5 e-commerce website. This project aims to provide a seamless and efficient shopping experience for PlayStation 5 enthusiasts.

## About the Project

This monorepo project contains multiple frontend applications and a backend server for the PS5 Store application. The frontend is developed using React, and the backend is developed using Flask (Python). This setup uses Yarn Workspaces for managing dependencies and scripts.

### Technologies Used

![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer%20Motion-black?style=flat&logo=framer&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![React Paginate](https://img.shields.io/badge/React%20Paginate-20232A?style=flat&logo=react&logoColor=61DAFB)
![React Redux](https://img.shields.io/badge/React%20Redux-764ABC?style=flat&logo=redux&logoColor=white)
![React Slick](https://img.shields.io/badge/React%20Slick-20232A?style=flat&logo=react&logoColor=61DAFB)
![React Toastify](https://img.shields.io/badge/React%20Toastify-20232A?style=flat&logo=react&logoColor=61DAFB)
![Redux Persist](https://img.shields.io/badge/Redux%20Persist-764ABC?style=flat&logo=redux&logoColor=white)
![Slick Carousel](https://img.shields.io/badge/Slick%20Carousel-20232A?style=flat&logo=react&logoColor=61DAFB)
![Tailwind Scrollbar](https://img.shields.io/badge/Tailwind%20Scrollbar-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

## Project Structure


```txt
/frontend
    - package.json
    - yarn.lock

  - /admin_login
    - package.json
    - ...
  - /managment
    - package.json
    - ...
  - /staff
    - package.json
    - ...
  - /store
    - /public
    - /src
    - package.json
    - ...
```

## Key Takeaways
- Using React Technology for a responsive Web Application.
- Emphasis on sleek design and functionality
- Best practices to enhance user experience and ensure success
- Continuous improvement driven by user feedback and performance monitoring

## Sleek Design Meets Functionality
We intended to have the website look stylish with easy-to-use functionalities. Users surfing it comfortably can browse through PlayStation 5 consoles, games, and accessories.

### Components of Design
- Lists consoles, games, and accessories with images
- User-friendly interface ensuring smooth navigation

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

## Prerequisites

- Node.js and Yarn

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
    localStorage.setItem('user', response.data);
    localStorage.setItem('token', response.data.token);
    window.location.href = '/';
  } catch (error) {
    console.error('Error logging in', error);
  }
};
```

## Acknowledgements

- **Company:** [AlX a sand company](https://www.alxafrica.com/)
- **Frontend Developer:** Zerihun Shiferaw ([Zed-bard](https://github.com/Zed-bard))
- **Backend Developer:** Waheed Khaled ([Wehda23](https://github.com/Wehda23))

### Community

- [React](https://reactjs.org/)
- [Yarn Workspaces](https://classic.yarnpkg.com/en/docs/workspaces/)
- [Concurrently](https://www.npmjs.com/package/concurrently)
