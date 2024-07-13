import { useState } from 'react';
import { ILoginUserForm } from '../services/api/RequestData';
import { IUserInformation } from '../services/api/ResponseData';
import loginUserApi from '../services/api/users/LoginUser';
import { useNavigate } from 'react-router';

interface IUseLogin {
    login: (body: ILoginUserForm) => Promise<void>;
    loading: boolean;
    error: string | null;
    success: boolean;
}

const useLogin = (): IUseLogin => {
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<boolean>(false);
    const navigate = useNavigate();

    const login = async (body: ILoginUserForm) => {
        setLoading(true);
        setError(null);
        setSuccess(false);

        try {
            const user: IUserInformation = await loginUserApi(body);
            console.log(user);
            // Save to Local Storage
            localStorage.setItem('user', JSON.stringify(user));
            setSuccess(true);
            navigate("/")
        } catch (error) {
            setError('Failed to log in');
            console.error('Login error:', error);
        } finally {
            setLoading(false);
        }
    };

    return { login, loading, error, success };
};

export default useLogin;
