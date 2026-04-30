import React, { useState } from "react";
import { analyzeResume } from "../api";
import ResultCard from "./ResultCard";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    try {
      setLoading(true);

      const res = await analyzeResume(file);

      setResult(res.data);
    } catch (error) {
      console.error(error);
      alert("Something went wrong (Backend issue)");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center" }}>
      
      {/* Title */}
      <h1 style={{ fontSize: "28px", marginBottom: "20px" }}>
        🚀 AI Resume Analyzer
      </h1>

      {/* Upload Box */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          gap: "10px",
          marginBottom: "20px"
        }}
      >
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          style={{
            padding: "10px",
            border: "1px solid #ddd",
            borderRadius: "8px",
            background: "#fff"
          }}
        />

        <button
          onClick={handleSubmit}
          style={{
            padding: "10px 20px",
            border: "none",
            borderRadius: "8px",
            background: "#4f46e5",
            color: "white",
            fontWeight: "bold",
            cursor: "pointer"
          }}
        >
          Analyze
        </button>
      </div>

      {/* Loader */}
      {loading && (
        <p style={{ color: "#555" }}>Analyzing your resume... ⏳</p>
      )}

      {/* Result */}
      {result && (
        <ResultCard
          jobs={result.jobs}
          suggestions={result.suggestions}
          ats_score={result.ats_score}
        />
      )}
    </div>
  );
}

export default UploadResume;