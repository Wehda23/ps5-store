import { createBrowserRouter } from "react-router-dom";
import LoginScreen from "./LoginPage/LoginPage";
import RegisterScreen from "./RegisterPage/RegisterPage";


const router = createBrowserRouter([
    {
      path: "/login",
      element: <LoginScreen/>,
    },
    {
      path: "/register",
      element: <RegisterScreen/>,
    },
  ]);



export default router;

