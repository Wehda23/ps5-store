import { useState } from "react";
import Loading from "./Loading";
import Button from "./ui/Button";
import Form from "./ui/Form";
import TextInput from "./ui/TextInput";
import useLogin from "../hooks/useLogin";
import { ILoginUserForm } from "../services/api/RequestData";
import Text from "./ui/Text";
import Break from "./ui/Break";
import BasicHeader from "./ui/BasicHeader";

function LoginForm(): JSX.Element {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const { login, loading, error, success } = useLogin();

    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();
        const loginUserForm: ILoginUserForm = { email, password };
        login(loginUserForm);
    };

    return (
        <>
        <Form className="w-full mx-auto p-8 bg-white shadow-lx rounded-lg">
            <BasicHeader>Login</BasicHeader>
            <Break />
            {loading && <Loading />}
            {error && <Text type="error">{error}</Text>}
            {success && <Text type='success'>Login successful!</Text>}
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
