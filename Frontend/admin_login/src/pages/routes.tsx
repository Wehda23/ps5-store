import { createBrowserRouter } from "react-router-dom";
import LoginScreen from "./LoginPage/LoginPage";
import RegisterScreen from "./RegisterPage/RegisterPage";
import ErrorPage from "./ErrorPage/ErrorPage";
import UserActions from "../utils/UserAction";

const router = createBrowserRouter([
    {
      path: "/login",
      element: <LoginScreen/>,
      errorElement: <ErrorPage />,
      loader: UserActions,
    },
    {
      path: "/register",
      element: <RegisterScreen/>,
      errorElement: <ErrorPage />,
      loader: UserActions,
    },
  ]);



export default router;

