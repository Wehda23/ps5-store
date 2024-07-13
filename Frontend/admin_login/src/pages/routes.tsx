import { createBrowserRouter } from "react-router-dom";
import LoginScreen from "./LoginPage/LoginPage";
import RegisterScreen from "./RegisterPage/RegisterPage";
import ErrorPage from "./ErrorPage/ErrorPage";
import UserLoader from "./UserLoader";

const router = createBrowserRouter([
    {
      path: "/login",
      element: <LoginScreen/>,
      errorElement: <ErrorPage />,
      loader: UserLoader,
    },
    {
      path: "/register",
      element: <RegisterScreen/>,
      errorElement: <ErrorPage />,
      loader: UserLoader,
    },
  ]);



export default router;

