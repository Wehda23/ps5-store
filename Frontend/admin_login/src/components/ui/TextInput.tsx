import React from "react";

interface IProps {
    label: string;
    value: string;
    onChange: (value: string) => void;
    maxLength?: number;
    type?: string;
    placeHolder?: string;
    disabled?: boolean;
    labelClassName?: string;
    inputClassName?: string;
    pattern?: string;
    required?: boolean;
    autoFocus?: boolean;
    readOnly?: boolean;
}

const TextInput: React.FC<IProps> = ({
    label,
    value,
    onChange,
    maxLength = 100,
    type = 'text',
    placeHolder = '',
    disabled = false,
    labelClassName = '',
    inputClassName = '',
    pattern,
    required = false,
    autoFocus = false,
    readOnly = false
}: IProps): JSX.Element => {

    return (
        <div className="mb-4">
            <label
            className={`block text-sm font-medium text-gray-700 ${labelClassName}`}
            >
            {label}
            </label>
            <input
                type={type}
                disabled={disabled}
                placeholder={placeHolder}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                maxLength={maxLength}
                className={`mt-1 p-2 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md ${inputClassName}`}
                pattern={pattern}
                required={required}
                autoFocus={autoFocus}
                readOnly={readOnly}
            />
        </div>
    );
}

export default TextInput;
