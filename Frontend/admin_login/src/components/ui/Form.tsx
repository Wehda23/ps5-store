import { ReactNode } from "react";

type FormProps = {
    children: ReactNode;
    className?: string;
}

function Form({ children, className = "" }: FormProps): JSX.Element {
    return (
        <form className={`p-4 bg-white shadow-md rounded ${className}`}>
            {children}
        </form>
    );
}

export default Form;
