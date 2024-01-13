import { useState } from "react";
import {
  Button,
  TextField,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";

const TraineeForm = () => {
  const [name, setName] = useState("");
  const [assetId, setAssetId] = useState("");

  const handleOptIn = () => {
    // Validate the form fields
    if (name && assetId) {
      // Send the opt-in request to the server (not implemented here)
      alert("Opt-in request sent successfully!");
    } else {
      alert("Please fill in all fields.");
    }
  };

  return (
    <div>
      <h2>Opt-In to Certificate</h2>
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
      <Button variant="contained" color="primary" onClick={handleOptIn}>
        Opt-In
      </Button>
    </div>
  );
};

export default TraineeForm;
