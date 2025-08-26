import { api, setAuthToken } from "@/lib/api";

export async function login(username: string, password: string) {
  const { data } = await api.post("/auth/token/", { username, password });
  setAuthToken(data.access);
  return data; // {access, refresh}
}