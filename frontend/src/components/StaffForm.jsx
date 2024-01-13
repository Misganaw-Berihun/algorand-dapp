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

  const handleCreateTrainee = async () => {
    // Validate the form fields
    if (newTrainee.name && newTrainee.email) {
      try {
        // Make a request to create a trainee in the backend
        const response = await fetch("http://localhost:8000/create_trainee", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newTrainee),
        });

        if (response.ok) {
          // If the trainee is successfully created, add it to the list with status 'in_progress'
          const traineeData = await response.json();
          onTraineeApproval({ ...traineeData, status: "in_progress" });
          setNewTrainee({ name: "", email: "" });
          alert("Trainee created successfully!");
        } else {
          alert("Error creating trainee");
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred.");
      }
    } else {
      alert("Please fill in all fields.");
    }
  };

  const handleTraineeApproval = (trainee) => {
    // Pass the trainee to the backend for further processing
    // For example, you may want to send an approval request to the backend
    // and update the trainee status based on the backend response
    // onTraineeApproval(trainee);
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
