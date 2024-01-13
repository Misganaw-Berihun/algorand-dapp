import { useState } from "react";
import StaffForm from "./components/StaffForm";
import TraineeForm from "./components/TraineeForm";
import { Button } from "@mui/material";

const App = () => {
  const [approvedTrainees, setApprovedTrainees] = useState([]);
  const [trainees, setTrainees] = useState([]);
  const [activeRole, setActiveRole] = useState(null);

  const handleTraineeApproval = (trainee) => {
    setApprovedTrainees((prevTrainees) => [...prevTrainees, trainee]);
  };

  const handleRoleSelection = (role) => {
    setActiveRole(role);
  };

  return (
    <div style={{ margin: "100px 400px" }}>
      <div
        style={{
          textAlign: "right",
          marginBottom: "10px",
        }}
      >
        <Button
          variant={activeRole === "staff" ? "contained" : "outlined"}
          color="primary"
          onClick={() => handleRoleSelection("staff")}
        >
          Staff Role
        </Button>
        <Button
          variant={activeRole === "trainee" ? "contained" : "outlined"}
          color="primary"
          onClick={() => handleRoleSelection("trainee")}
        >
          Trainee Role
        </Button>
      </div>

      {activeRole === "staff" && (
        <StaffForm
          trainees={trainees}
          onTraineeApproval={handleTraineeApproval}
        />
      )}

      {activeRole === "trainee" && (
        <>
          <TraineeForm optedInTrainees={approvedTrainees} />
          {approvedTrainees.length > 0 && (
            <div>
              <h3>Approved Trainees</h3>
              <ul>
                {approvedTrainees.map((trainee, index) => (
                  <li key={index}>{trainee.name}</li>
                ))}
              </ul>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default App;
