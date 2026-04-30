import React from "react";

function ResultCard({ jobs = [], suggestions = "", ats_score = 0 }) {
  return (
    <div style={{ marginTop: "30px", textAlign: "left" }}>
      
      <h2 style={{ marginBottom: "20px", color: "#222" }}>
        📊 Results
      </h2>

      {/* ATS CARD */}
      <div
        style={{
          padding: "20px",
          borderRadius: "16px",
          background: "#ffffff",
          boxShadow: "0 6px 18px rgba(0,0,0,0.1)",
          marginBottom: "25px"
        }}
      >
        <h3>📈 ATS Score</h3>

        <div style={{ fontSize: "28px", fontWeight: "bold" }}>
          {ats_score}/100
        </div>

        <div
          style={{
            height: "10px",
            background: "#eee",
            borderRadius: "5px",
            marginTop: "10px"
          }}
        >
          <div
            style={{
              width: `${ats_score}%`,
              height: "100%",
              background:
                ats_score > 70
                  ? "#22c55e"
                  : ats_score > 40
                  ? "#f59e0b"
                  : "#ef4444",
              borderRadius: "5px"
            }}
          />
        </div>
      </div>

      {/* JOBS */}
      <div style={{ marginBottom: "25px" }}>
        <h3>💼 Recommended Jobs</h3>

        {jobs.length > 0 ? (
          jobs.map((job, index) => (
            <div
              key={index}
              style={{
                padding: "15px",
                margin: "10px 0",
                borderRadius: "12px",
                background: "#fff",
                border: "1px solid #eee",
                boxShadow: "0 3px 10px rgba(0,0,0,0.06)",
                transition: "0.3s"
              }}
            >
              {job}
            </div>
          ))
        ) : (
          <p>No jobs found</p>
        )}
      </div>

      {/* AI SUGGESTIONS */}
      <div>
        <h3>🤖 AI Suggestions</h3>

        <div
          style={{
            padding: "18px",
            borderRadius: "12px",
            background: "#f8fafc",
            border: "1px solid #e2e8f0",
            whiteSpace: "pre-line",
            lineHeight: "1.6"
          }}
        >
          {suggestions || "No suggestions available"}
        </div>
      </div>
    </div>
  );
}

export default ResultCard;