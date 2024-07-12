import { redirect } from "react-router-dom";
import { IUserInformation } from "../services/api/ResponseData";


interface IUserDetailsAction {
    (): Promise<Response>;
}

const UserActions: IUserDetailsAction = async (): Promise<Response> => {
    const user = localStorage.getItem("User");
    if (user) {
        const userInfo: IUserInformation = JSON.parse(user);
        console.log("User is logged in:", userInfo);
        return redirect("/");
    }
    return new Response();
}

export default UserActions;
