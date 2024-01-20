import { useState } from "react";
import { Button, TextField, CircularProgress } from "@mui/material";

const TraineeForm = () => {
  const [name, setName] = useState("");
  const [assetId, setAssetId] = useState("");
  const [loading, setLoading] = useState(false);

  const handleOptIn = async () => {
    if (name && assetId) {
      try {
        setLoading(true);

        // Replace the hardcoded email with the actual trainee's email
        const traineeEmail = "misganawbmb@gmail.com"; // Get this from user input or authentication

        const response = await fetch("http://127.0.0.1:8000/opt_in", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: name,
            asset_id: assetId,
            email: traineeEmail,
          }),
        });

        if (response.ok) {
          alert("Opt-in request sent successfully!");
          setName("");
          setAssetId("");
        } else {
          const errorMessage = await response.text();
          alert(`Error opting in trainee: ${errorMessage}`);
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred.");
      } finally {
        setLoading(false);
      }
    } else {
      alert("Please fill in all fields.");
    }
  };

  return (
    <div>
      <h2>Get Certificate</h2>
      <TextField
        label="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <TextField
        label="Asset ID"
        value={assetId}
        onChange={(e) => setAssetId(e.target.value)}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleOptIn}
        disabled={loading}
      >
        {loading ? <CircularProgress size={24} /> : "Opt-In"}
      </Button>
    </div>
  );
};

export default TraineeForm;
