import React, { ReactNode } from "react";


interface IProps {
    children: ReactNode;
    className?: string;
}

const Section: React.FC<IProps> = ({children, className}): JSX.Element => {
    return (
        <section className={className}>
            {children}
        </section>
    )
}


export default Section;