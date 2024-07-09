// loginUser.ts

import { psFetch, Data } from '../../utils/storeFetch';
import DOMAIN from '../../settings';

const loginUser = async (body: Data) => {
    const url: string = DOMAIN + '/api/users/login';
    const headers: Data = {
        'Content-Type': 'application/json' // Assuming JSON content type
    };

    try {
        const responseData = await psFetch.post(url, headers, body); // Automatically handles JSON parsing
        console.log(responseData);
        return responseData; // Return the parsed response data
    } catch (error) {
        console.error('Error logging in:', error);
        throw error; // Re-throw the error for handling elsewhere if needed
    }
};

export default loginUser;
