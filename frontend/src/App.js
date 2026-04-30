import UploadResume from "./components/UploadResume";

function App() {
  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundImage: "url('/background_for_ai_resume_analyzer.jpg')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: "20px"
      }}
    >
      {/* Glass Container */}
      <div
        style={{
          width: "100%",
          maxWidth: "950px",
          background: "rgba(255,255,255,0.92)",
          backdropFilter: "blur(12px)",
          padding: "35px",
          borderRadius: "18px",
          boxShadow: "0 10px 30px rgba(0,0,0,0.25)"
        }}
      >
        <UploadResume />
      </div>
    </div>
  );
}

export default App;