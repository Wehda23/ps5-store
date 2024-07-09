// Create a Proxy Pattern Design Class to fetch data from API endpoints

export interface Data {
    [key: string]: any;
}

interface Request {
    (url: string, headers: Data, body: Data): Promise<Data[] | Data>;
}

interface GetRequest {
    (url: string, headers: Data): Promise<Data[] | Data>;
}

type DeleteRequest = GetRequest;

interface IPSFetch {
    get: GetRequest;
    post: Request;
    put: Request;
    delete: DeleteRequest;
}

class PSFetch implements IPSFetch {
    async get(url: string, headers: Data): Promise<Data[] | Data> {
        console.log("get method called");
        const response = await fetch(url, {
            method: 'GET',
            headers: headers
        });

        return response.json(); // Automatically parses JSON response
    }

    async post(url: string, headers: Data, body: Data): Promise<Data[] | Data> {
        console.log("post method called");
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body)
        });

        return response.json(); // Automatically parses JSON response
    }

    async put(url: string, headers: Data, body: Data): Promise<Data[] | Data> {
        console.log("put method called");
        const response = await fetch(url, {
            method: 'PUT',
            headers: headers,
            body: JSON.stringify(body)
        });

        return response.json(); // Automatically parses JSON response
    }

    async delete(url: string, headers: Data): Promise<Data[] | Data> {
        console.log("delete method called");
        const response = await fetch(url, {
            method: 'DELETE',
            headers: headers
        });

        return response.json(); // Automatically parses JSON response
    }
}

export const psFetch = new PSFetch();
