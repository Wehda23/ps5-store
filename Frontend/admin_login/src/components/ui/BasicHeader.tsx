import React, { ReactNode } from "react";


interface IProps {
    children: ReactNode;
    className?: string;
}

const BasicHeader: React.FC<IProps> = ({children, className="text-2xl font-bold text-center mb-4"}) => {
    return (
        <h1 className={className}>{children}</h1>
    )
}


export default BasicHeader;