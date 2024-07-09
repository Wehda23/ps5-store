// File contains Request body data structure or Interfaces

// for the API endpoints

export interface ILoginUserForm {
    email: string;
    password: string;
}

export interface IRegisterationForm {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
}