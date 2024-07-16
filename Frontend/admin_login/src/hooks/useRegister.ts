import { useState } from 'react';
import { IRegisterationForm } from '../services/api/RequestData';
import { IRegisterationResponse } from '../services/api/ResponseData';
import registerUserApi from '../services/api/users/RegisterUser';

interface IUseRegister {
    register: (body: IRegisterationForm) => Promise<void>;
    loading: boolean;
    error: string | null;
    success: boolean;
}

const useRegister = (): IUseRegister => {
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<boolean>(false);

    const register = async (body: IRegisterationForm) => {
        setLoading(true);
        setError(null);
        setSuccess(false);

        try {
            const response: IRegisterationResponse = await registerUserApi(body);
            console.log(response);
            setSuccess(true);
        } catch (error) {
            setError('Failed to register account');
            console.error('Account Registeration error:', error);
        } finally {
            setLoading(false);
        }
    };

    return { register, loading, error, success };
};

export default useRegister;
