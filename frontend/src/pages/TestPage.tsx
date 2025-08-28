import { useState } from "react";
import { api, setAuthToken } from "@/lib/api";

export default function TestPage() {
  const [status, setStatus] = useState("");

  const handleLogin = async () => {
    setStatus("Logging in...");
    try {
      const { data } = await api.post("/auth/token/", {
        username: "admin",       // đổi theo superuser bạn tạo
        password: "yourpass"
      });
      setAuthToken(data.access);
      setStatus("✅ Login OK, access token saved");
    } catch (err: any) {
      setStatus("❌ Login failed: " + (err.response?.data?.detail || err.message));
    }
  };

  const handleList = async () => {
    setStatus("Fetching scores...");
    try {
      const res = await api.get("/scores/?page=1");
      setStatus(JSON.stringify(res.data.results, null, 2));
    } catch (err: any) {
      setStatus("❌ List failed: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Test API Page</h1>
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleList} style={{ marginLeft: 10 }}>List Scores</button>
      <pre style={{ marginTop: 20, background: "#111", color: "#0f0", padding: 10 }}>
        {status}
      </pre>
    </div>
  );
}
