import { useState, useEffect } from "react";
import { Button, TextField, CircularProgress } from "@mui/material";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";

const StaffForm = ({ trainees }) => {
  const [newTrainee, setNewTrainee] = useState({
    name: "",
    email: "",
  });
  const [optInList, setOptInList] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Fetch the list of trainees who have opted in from the backend
    const fetchOptInList = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/opt_in_list");
        if (response.ok) {
          const optInListData = await response.json();
          setOptInList(optInListData);
        } else {
          console.error("Error fetching opt-in list");
        }
      } catch (error) {
        console.error("Error fetching opt-in list:", error);
      }
    };

    fetchOptInList();
  }, []);

  const handleApprove = async (assetId) => {
    try {
      // Call the backend endpoint to approve the opt-in request
      const response = await fetch("http://127.0.0.1:8000/transfer_asset", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          asset_id: assetId,
          name: "TraineeName",
          email: "trainee@example.com",
        }),
      });

      if (response.ok) {
        // Update the user state to reflect approval
        setOptInList((prevList) =>
          prevList.map((trainee) =>
            trainee.assetId === assetId
              ? { ...trainee, state: "approved" }
              : trainee
          )
        );
        alert("Opt-in request approved successfully!");
      } else {
        console.error("Error approving opt-in request");
      }
    } catch (error) {
      console.error("Error approving opt-in request:", error);
    }
  };

  const handleDecline = async (assetId) => {
    try {
      // Call the backend endpoint to decline the opt-in request
      const response = await fetch("http://127.0.0.1:8000/decline_opt_in", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: "TraineeName",
          email: "trainee@example.com",
        }),
      });

      if (response.ok) {
        // Update the user state to reflect decline
        setOptInList((prevList) =>
          prevList.map((trainee) =>
            trainee.assetId === assetId
              ? { ...trainee, state: "declined" }
              : trainee
          )
        );
        alert("Opt-in request declined successfully!");
      } else {
        console.error("Error declining opt-in request");
      }
    } catch (error) {
      console.error("Error declining opt-in request:", error);
    }
  };

  const handleCreateTrainee = async () => {
    console.log("New Trainee:");
    console.log(newTrainee);

    if (newTrainee.name && newTrainee.email) {
      try {
        setLoading(true);

        const response = await fetch("http://127.0.0.1:8000/create_trainee", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newTrainee),
        });

        if (response.ok) {
          setNewTrainee({ name: "", email: "" });
          alert("Trainee created successfully!");
        } else {
          const errorMessage = await response.text();
          alert(`Error creating trainee: ${errorMessage}`);
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
      <h2>Create New Trainee</h2>
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
      <Button
        variant="contained"
        color="primary"
        onClick={handleCreateTrainee}
        disabled={loading}
      >
        {loading ? <CircularProgress size={24} /> : "Create New Trainee"}
      </Button>

      <div>
        <h2>Opt-In Requests</h2>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {optInList.map((trainee) => (
                <TableRow key={trainee.assetId}>
                  <TableCell>{trainee.email}</TableCell>
                  <TableCell>
                    {trainee.state === "approved" ? (
                      "Approved"
                    ) : trainee.state === "declined" ? (
                      "Declined"
                    ) : (
                      <>
                        <Button
                          variant="contained"
                          color="primary"
                          onClick={() => handleApprove(trainee.assetId)}
                        >
                          Approve
                        </Button>
                        <Button
                          variant="contained"
                          color="secondary"
                          onClick={() => handleDecline(trainee.assetId)}
                        >
                          Decline
                        </Button>
                      </>
                    )}
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
