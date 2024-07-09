export interface Data {
    [key: string]: any;
}

export interface IToken {
    access: string;
    refresh: string;
}

export interface IUserInformation {
    first_name: string;
    last_name: string;
    email: string;
    token: IToken;
}

export type ResponseData = Data[] | Data | string | IUserInformation;
