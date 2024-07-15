import LoginForm from "../../components/LoginForm";
import Container from "../../components/ui/Container";
import Screen from "../../components/ui/Screen";


function LoginScreen(): JSX.Element {
    return (
    <Screen className="flex flex-col items-center justify-center space-y-4 w-lvw md:flex-row md:space-x-4 md:space-y-0">
        <Container className="w-11/12 md:w-3/12">
            <LoginForm />
        </Container>
        <Container className="w-11/12 md:w-3/12">
            <LoginForm />
        </Container>
    </Screen>
    )
}

export default LoginScreen;