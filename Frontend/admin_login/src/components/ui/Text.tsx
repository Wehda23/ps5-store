import React, { ReactNode } from "react"

export type TextTypes = "error" | "info" | "warning" | "success" | "danger"

interface IProps {
    children: ReactNode;
    type: TextTypes;
}

export interface TextColors {
    error: "text-red-500",
    info: "text-blue-500",
    warning: "text-orange-500",
    success: "text-green-500",
    danger: "text-red-500"
}

const colors: TextColors = {
    error: "text-red-500",
    info: "text-blue-500",
    warning: "text-orange-500",
    success: "text-green-500",
    danger: "text-red-500"
}

const Text: React.FC<IProps> = ({children, type}) => {
    return (
        <div className={`${colors[type]}  mb-4`}>{children}</div>
    )
}

export default Text;