import LoginForm from "../../components/LoginForm";
import Container from "../../components/ui/Container";
import Screen from "../../components/ui/Screen";
import Section from "../../components/ui/Section";
import { project } from "../../settings";


function LoginScreen(): JSX.Element {
    return (
    <Screen className="flex flex-col items-center space-y-10 w-lvw mb-20">
        <Section className="w-lvw flex flex-col items-center justify-center shadow-lg shadow-slate-300 rounded-sm h-auto">
            <img src={`${project === 'testing' ? "/src" : ""}/images/ps5-family-image-block-01-en-16sep20.webp`} className="w-auto"/>
        </Section>
        <Section className="container flex flex-col items-center justify-center">
            <Container className="w-11/12 lg:w-5/12">
                <LoginForm />
            </Container>
        </Section>
    </Screen>
    )
}

export default LoginScreen;