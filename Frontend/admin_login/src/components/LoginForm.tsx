import { useState } from "react";
import Loading from "./Loading";
import Button from "./ui/Button";
import Form from "./ui/Form";
import TextInput from "./ui/TextInput";
import useLogin from "../hooks/useLogin";
import { ILoginUserForm } from "../services/api/RequestData";

function LoginForm(): JSX.Element {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const { login, loading, error, success } = useLogin();
    console.log("render");
    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();
        const loginUserForm: ILoginUserForm = { email, password };
        login(loginUserForm);
    };

    return (
        <>
        <Form className="w-full max-w-sm mx-auto p-8 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold text-center mb-4">Login</h1>
            <hr className="mb-6 border-t-2 border-gray-300"/>
            {loading && <Loading />}
            {error && <div className="text-red-500 mb-4">{error}</div>}
            {success && <div className="text-green-500 mb-4">Login successful!</div>}
            <TextInput
                label="Email"
                type="email"
                value={email}
                onChange={setEmail}
                placeHolder="Enter your email"
                required
            />
            <TextInput
                label="Password"
                type="password"
                value={password}
                onChange={setPassword}
                placeHolder="Enter your password"
                required
            />
            <Button
                onClick={handleSubmit}
                text="Login"
                className="w-full mt-4 bg-blue-500 hover:bg-blue-700"
            />
        </Form>
        </>
    )
}

export default LoginForm;
