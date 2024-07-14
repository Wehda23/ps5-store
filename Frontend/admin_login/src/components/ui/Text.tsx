import React, { ReactNode } from "react"

export type TextTypes = "error" | "info" | "warning" | "success" | "danger"

interface IProps {
    children: ReactNode;
    type: TextTypes;
}

export interface TextColors {
    error: "text-red-500 mb-4",
    info: "text-blue-500 mb-4",
    warning: "text-orange-500 mb-4",
    success: "text-green-500 mb-4",
    danger: "text-red-500 mb-4"
}

const colors: TextColors = {
    error: "text-red-500 mb-4",
    info: "text-blue-500 mb-4",
    warning: "text-orange-500 mb-4",
    success: "text-green-500 mb-4",
    danger: "text-red-500 mb-4"
}

const Text: React.FC<IProps> = ({children, type}) => {
    return (
        <div className={`${colors[type]}`}>{children}</div>
    )
}

export default Text;