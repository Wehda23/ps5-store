// loginUser.ts

import psFetch from '../StoreFetch';
import { ResponseData, Data, IUserInformation } from '../ResponseData';
import DOMAIN from '../../../settings';



const loginUser = async (body: Data) => {
    const url: string = DOMAIN + '/api/users/login';
    const headers: Data = {
        'Content-Type': 'application/json' // Assuming JSON content type
    };

    try {
        const responseData: ResponseData = await psFetch.post(url, headers, body); // Automatically handles JSON parsing
        console.log(responseData);

        if(typeof responseData === 'object' && 'first_name' in responseData && 'token' in responseData){
            return responseData as IUserInformation;
        } else {
            throw new Error('Invalid response format');
        }
    } catch (error) {
        console.error('Error logging in:', error);
        throw error; // Re-throw the error for handling elsewhere if needed
    }
};

export default loginUser;
