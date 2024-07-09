// loginUser.ts

import {psFetch, Data} from '../../utils/storeFetch';
import DOMAIN from '../../settings';



const loginUser = async (body: Data) => {
    const url: string = DOMAIN + '/api/users/login';
    const headers: Data = {
        'Content-Type': 'application/json' // Assuming JSON content type
    };

    try {
        const response = await psFetch.post(url, headers, body);
        const responseData = await response.json(); // Parse JSON response
        console.log(responseData);
        return responseData; // Return the parsed response data
    } catch (error) {
        console.error('Error logging in:', error);
        throw error; // Re-throw the error for handling elsewhere if needed
    }
};

export default loginUser;
