import React, { ReactNode } from "react";


interface IProps {
    children: ReactNode;
    className?: string;
}

const Container: React.FC<IProps> = ({children, className = ""}): JSX.Element => {
    return (
        <div className={className}>{children}</div>
    )
}

export default Container;