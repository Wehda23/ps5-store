// Create a Proxy Pattern Design Class to fetch data from API endpoints

interface Data {
    [key: string]: any;
}

interface Request {
    (url: string, headers: Data, body: Data): Promise<Response>;
}

interface GetRequest {
    (url: string, headers: Data): Promise<Response>;
}

type DeleteRequest = GetRequest

interface IPSFetch {
    get: GetRequest;
    post: Request;
    put: Request;
    delete: DeleteRequest;
}

class PSFetch implements IPSFetch {
    async get(url: string, headers: Data): Promise<Response> {
        console.log("get method called");
        return fetch(url, {
            method: 'GET',
            headers: headers
        });
    }

    async post(url: string, headers: Data, body: Data): Promise<Response> {
        console.log("post method called");
        return fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body)
        });
    }

    async put(url: string, headers: Data, body: Data): Promise<Response> {
        console.log("put method called");
        return fetch(url, {
            method: 'PUT',
            headers: headers,
            body: JSON.stringify(body)
        });
    }

    async delete(url: string, headers: Data): Promise<Response> {
        console.log("delete method called");
        return fetch(url, {
            method: 'DELETE',
            headers: headers
        });
    }
}

export default PSFetch;