import React from "react";


interface IProps {
    text: string;
    onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
    className?: string;
    disabled?: boolean;
}

const Button: React.FC<IProps> = ({
    text,
    onClick,
    className="",
    disabled = false
}: IProps): JSX.Element => {

    return (
        <button
        className={`px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 disabled:bg-gray-400 disabled:cursor-not-allowed ${className}`}
        disabled={disabled}
        onClick={(e) => onClick(e)}
        >
            {text}
        </button>
    );
}

export default Button;