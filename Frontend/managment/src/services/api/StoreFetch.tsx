import { Data, ResponseData } from "./ResponseData";
// Create a Proxy Pattern Design Class to fetch data from API endpoints

interface Request {
    (url: string, headers: Data, body: Data): Promise<ResponseData>;
}

interface GetRequest {
    (url: string, headers: Data): Promise<ResponseData>;
}

type DeleteRequest = GetRequest;

interface IPSFetch {
    get: GetRequest;
    post: Request;
    put: Request;
    delete: DeleteRequest;
}

class PSFetch implements IPSFetch {
    async get(url: string, headers: Data): Promise<ResponseData> {
        console.log("get method called");
        const response = await fetch(url, {
            method: 'GET',
            headers: headers
        });

        return response.json(); // Automatically parses JSON response
    }

    async post(url: string, headers: Data, body: Data): Promise<ResponseData> {
        console.log("post method called");
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body)
        });

        return response.json(); // Automatically parses JSON response
    }

    async put(url: string, headers: Data, body: Data): Promise<ResponseData> {
        console.log("put method called");
        const response = await fetch(url, {
            method: 'PUT',
            headers: headers,
            body: JSON.stringify(body)
        });

        return response.json(); // Automatically parses JSON response
    }

    async delete(url: string, headers: Data): Promise<ResponseData> {
        console.log("delete method called");
        const response = await fetch(url, {
            method: 'DELETE',
            headers: headers
        });

        return response.json(); // Automatically parses JSON response
    }
}

const psFetch = new PSFetch();

export default psFetch;
