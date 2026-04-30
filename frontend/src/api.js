import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

export const analyzeResume = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/analyze/", formData);
};