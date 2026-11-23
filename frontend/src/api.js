
import axios from "axios";

const API = axios.create({
  baseURL:
    process.env.REACT_APP_API_URL ||
    "http://localhost:8000",
});

export const analyzeResume = (file) => {

  const formData = new FormData();

  formData.append("file", file);

  return API.post("/analyze/", formData);
};
