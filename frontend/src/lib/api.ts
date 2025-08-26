import axios from "axios"

export const api = axios.create({
    baseURL: "http://localhost:8000/api",
    withCredentials: false, // dùng JWT, không cần cookie
});

// Lưu token vào localStorage (hoặc Zustand/Context)
export const setAuthToken = (token?: string) => {
    if (token) localStorage.setItem("access_token", token);
    else localStorage.removeItem("access_token");
}


api.interceptors.request.use((config) => {
    const token = localStorage.getItem("access_token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
});