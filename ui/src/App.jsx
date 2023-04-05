import { MDBCol as Col, MDBRow as Row } from "mdbreact";
import "./App.css";
import AppRoutes from "./components/AppRoutes.jsx";
import Landing from "./components/Landing";

function App() {
  return (
    <Row className="vh-100 vw-100 align-items-center mx-0">
      <Col sm={3}>
        <Landing />
      </Col>
      <Col sm={9}>
        <AppRoutes id="app" />
      </Col>
    </Row>
  );
}

export default App;
