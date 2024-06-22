// src/integrationservice.js

const BASE_URL = 'http://127.0.0.1:5000';

// Utility function to handle fetch requests
async function fetchData(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch Error:', error);
        throw error;
    }
}

// Function to get users
export async function getUsers() {
    const url = `${BASE_URL}/users`;
    return fetchData(url);
}

// Function to create a new user
export async function createUser(user) {
    const url = `${BASE_URL}/users`;
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
    };
    return fetchData(url, options);
}

// Function to get orders
export async function getOrders() {
    const url = `${BASE_URL}/orders`;
    return fetchData(url);
}

// Function to create a new order
export async function createOrder(order) {
    const url = `${BASE_URL}/orders`;
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(order),
    };
    return fetchData(url, options);
}

