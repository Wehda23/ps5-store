import psFetch from "../StoreFetch";
import { IRegisterationForm } from "../RequestData";
import { IRegisterationResponse, Data, ResponseData } from "../ResponseData";
import DOMAIN from '../../../settings';



interface IRegisterUserAPI {
    (body: IRegisterationForm): Promise<IRegisterationResponse>
}

const registerUserApi: IRegisterUserAPI = async (body: IRegisterationForm): Promise<IRegisterationResponse> => {
    const url: string = DOMAIN + '/api/users/register';
    const headers: Data = {
        'Content-Type': 'application/json' // Assuming JSON content type
    };

    try {
        const responseData: ResponseData = await psFetch.post(url, headers, body); // Automatically handles JSON parsing
        console.log("Response: ",responseData);

        if(typeof responseData === 'object' &&  "message" in responseData){
            return responseData as IRegisterationResponse;
        } else {
            throw new Error('Invalid response format');
        }
    } catch (error) {
        console.error('Error Registeration:', error);
        throw error; // Re-throw the error for handling elsewhere if needed
    }
};

export default registerUserApi;