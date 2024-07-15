import React, { ReactNode } from "react";


interface IProps {
    children: ReactNode;
    className?: string;
}

const Screen: React.FC<IProps> = ({children, className = ""}): JSX.Element => {
    return (
        <div className={className}>{children}</div>
    )
}

export default Screen;