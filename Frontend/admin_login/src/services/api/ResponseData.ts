export interface Data {
    [key: string]: any;
}

export interface IToken {
    access: string;
    refresh: string;
}

export interface IShippingAddress extends Data {
    address: string;
    city: string;
    country: string;
    default: boolean;
    state: string;
}

type ShippingAddressID = number;

type ShippingAddresses = ShippingAddressID[] | IShippingAddress | IShippingAddress[];

export interface IUserInformation {
    first_name: string;
    last_name: string;
    email: string;
    token: IToken;
    shipping_addressess?: ShippingAddresses;
}

export type IRegisterationResponse = "Successful Registeration";

export type ResponseData = Data[] | Data | string | IUserInformation | IRegisterationResponse;
