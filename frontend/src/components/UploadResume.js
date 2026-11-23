
import React, { useState } from "react";
import { analyzeResume } from "../api";
import ResultCard from "./ResultCard";

function UploadResume() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {

    const selectedFile = e.target.files[0];

    setResult(null);
    setError("");

    if (!selectedFile) {
      setFile(null);
      return;
    }

    if (!selectedFile.name.toLowerCase().endsWith(".pdf")) {
      setFile(null);
      setError("Please upload a PDF file only.");
      e.target.value = "";
      return;
    }

    setFile(selectedFile);
  };


  const handleSubmit = async () => {

    if (!file) {
      setError("Please select a PDF resume first.");
      return;
    }

    try {

      setLoading(true);
      setError("");
      setResult(null);

      const res = await analyzeResume(file);

      setResult(res.data);

    } catch (err) {

      console.error("Resume Analysis Error:", err);

      setError(
        err.response?.data?.detail ||
        "Unable to analyze your resume. Please try again."
      );

    } finally {

      setLoading(false);

    }
  };


  return (

    <div style={{ textAlign: "center" }}>

      <h1 style={{ fontSize: "28px", marginBottom: "20px" }}>
        🚀 AI Resume Analyzer
      </h1>

      <p>
        Upload your resume and discover suitable career opportunities.
      </p>


      {/* FILE UPLOAD */}

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          gap: "10px",
          marginBottom: "20px",
          flexWrap: "wrap"
        }}
      >

        <input
          type="file"
          accept=".pdf,application/pdf"
          onChange={handleFileChange}
          disabled={loading}
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          style={{
            padding: "10px 20px",
            border: "none",
            borderRadius: "8px",
            background: loading ? "#999" : "#4f46e5",
            color: "white",
            fontWeight: "bold",
            cursor: loading ? "not-allowed" : "pointer"
          }}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

      </div>


      {/* SELECTED FILE */}

      {file && (
        <p>
          Selected file: <strong>{file.name}</strong>
        </p>
      )}


      {/* LOADING */}

      {loading && (
        <p style={{ color: "#555" }}>
          Analyzing your resume... Please wait.
        </p>
      )}


      {/* ERROR */}

      {error && (
        <p
          role="alert"
          style={{
            color: "#dc2626",
            background: "#fee2e2",
            padding: "12px",
            borderRadius: "8px"
          }}
        >
          {error}
        </p>
      )}


      {/* RESULTS */}

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
