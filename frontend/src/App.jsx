import { useState } from "react";
import StaffForm from "./components/StaffForm";
import TraineeForm from "./components/TraineeForm";
import { Button } from "@mui/material";
import styled from "styled-components";

const Container = styled.div`
  margin: 100px 400px;
`;

const RoleSelectionButtons = styled.div`
  text-align: right;
  margin-bottom: 10px;

  button {
    margin-left: 10px;
  }
`;

const App = () => {
  const [trainees, setTrainees] = useState([]);
  const [activeRole, setActiveRole] = useState(null);

  const handleRoleSelection = (role) => {
    setActiveRole(role);
  };

  return (
    <Container>
      <RoleSelectionButtons>
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
      </RoleSelectionButtons>

      {activeRole === "staff" && <StaffForm trainees={trainees} />}
      {activeRole === "trainee" && <TraineeForm />}
    </Container>
  );
};

export default App;
