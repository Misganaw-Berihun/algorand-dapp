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

const StaffForm = ({ trainees, onTraineeApproval }) => {
  const [newTrainee, setNewTrainee] = useState({
    name: "",
    email: "",
  });

  const handleCreateTrainee = () => {
    // Validate the form fields
    if (newTrainee.name && newTrainee.email) {
      // Add the new trainee to the list with status 'in_progress'
      onTraineeApproval({ ...newTrainee, status: "in_progress" });
      setNewTrainee({ name: "", email: "" });
    } else {
      alert("Please fill in all fields.");
    }
  };

  const handleTraineeApproval = (trainee) => {
    onTraineeApproval(trainee);
  };

  return (
    <div>
      <h2>Staff Role - Create New Trainee</h2>
      <TextField
        label="Name"
        value={newTrainee.name}
        onChange={(e) => setNewTrainee({ ...newTrainee, name: e.target.value })}
      />
      <TextField
        label="Email"
        value={newTrainee.email}
        onChange={(e) =>
          setNewTrainee({ ...newTrainee, email: e.target.value })
        }
      />
      <Button variant="contained" color="primary" onClick={handleCreateTrainee}>
        Create New Trainee
      </Button>

      <div style={{ marginTop: "20px" }}>
        <h3>Trainees List</h3>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {trainees.map((trainee, index) => (
                <TableRow key={index}>
                  <TableCell>{trainee.name}</TableCell>
                  <TableCell>{trainee.status}</TableCell>
                  <TableCell>
                    <Button
                      variant="contained"
                      color={
                        trainee.status === "opt-in"
                          ? "secondary"
                          : trainee.status === "approved"
                          ? "disabled"
                          : "primary"
                      }
                      disabled={
                        trainee.status === "approved" ||
                        trainee.status === "opt-in"
                      }
                      onClick={() => handleTraineeApproval(trainee)}
                    >
                      {trainee.status === "opt-in"
                        ? "Opt-In"
                        : trainee.status === "approved"
                        ? "Approved"
                        : "Approve"}
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>
  );
};

export default StaffForm;
