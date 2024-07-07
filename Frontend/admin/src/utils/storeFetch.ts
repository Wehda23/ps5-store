// Create a Proxy Pattern Design Class to fetch data from API endpoints


interface IPSFetch {
    get(): void;
    post(): void;
    put(): void;
    delete(): void;
}

class PSFetch implements IPSFetch{

    get(){
        console.log("get method called");
    }
    post(){
        console.log("post method called");
    }
    put(){
        console.log("put method called");
    }
    delete(){
        console.log("delete method called");
    }
}


export default PSFetch;