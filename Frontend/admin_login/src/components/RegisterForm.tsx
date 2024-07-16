import { useState } from "react";
import Form from "./ui/Form";
import Text from "./ui/Text";
import TextInput from "./ui/TextInput";
import Button from "./ui/Button";
import BasicHeader from "./ui/BasicHeader";
import Break from "./ui/Break";
import useRegister from "../hooks/useRegister";
import Loading from "./Loading";
import { IRegisterationForm } from "../services/api/RequestData";


function RegisterForm(): JSX.Element {
    const [password, setPassword] = useState<string>("");
    const [passwordConfirm, setPasswordConfirm] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [firstName, setFirstName] = useState<string>("");
    const [lastName, setLastName] = useState<string>("");
    const {register, loading, error, success} = useRegister();

    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {3
        event.preventDefault()
        const registerationForm: IRegisterationForm = {
            email: email,
            password: password,
            first_name: firstName,
            last_name: lastName
        }
        register(registerationForm)
    }
    return (
        <Form>
            <BasicHeader>Register</BasicHeader>
            <Break/>
            {loading && <Loading />}
            {error && <Text type="error">{error}</Text>}
            {success && <Text type='success'>Registeration is successful!</Text>}
            <TextInput
            label="First Name"
            value={firstName}
            onChange={setFirstName}
            required
            placeHolder="Enter your first name"
            />
            <TextInput
            label="Last Name"
            value={lastName}
            onChange={setLastName}
            required
            placeHolder="Enter your last name"
            />
            <TextInput
            label="Email"
            value={email}
            onChange={setEmail}
            required
            placeHolder="Enter your email address"
            />
            <TextInput
            label="Password"
            value={password}
            onChange={setPassword}
            type="password"
            required
            placeHolder="Enter your password"
            />
            <TextInput
            label="Confirm Password"
            value={passwordConfirm}
            onChange={setPasswordConfirm}
            type="password"
            required
            placeHolder="Confirm your password"
            />
            {
            passwordConfirm !== password
            && <Text type="warning">Passwords Do not match</Text>
            }
            {
            password.length > 6 && passwordConfirm === password
            && <Text type="success">Passwords Match</Text>
            }
            <Button
            onClick={handleSubmit}
            text='Register'
            className="w-full mt-4 bg-blue-500 hover:bg-blue-700"
            disabled={!(password.length > 6 && passwordConfirm === password)}
            />
        </Form>
    )
}


export default RegisterForm;