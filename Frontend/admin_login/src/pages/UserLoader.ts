import { redirect } from "react-router-dom";
import { IUserInformation } from "../services/api/ResponseData";


interface IUserDetailsLoader {
    (): Promise<Response>;
}

const UserLoader: IUserDetailsLoader = async (): Promise<Response> => {
    const user = localStorage.getItem("user");
    if (user) {
        const userInfo: IUserInformation = JSON.parse(user);
        console.log("User is logged in:", userInfo);
        return redirect("/");
    }
    console.log("UserLoader User does not exist.")
    return new Response();
}

export default UserLoader;
