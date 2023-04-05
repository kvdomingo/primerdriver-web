import { MDBCol as Col, MDBRow as Row } from "mdbreact";
import "./App.css";
import Landing from "./components/Landing";
import Station from "./components/Station";

function App() {
  return (
    <Row className="vh-100 vw-100 align-items-center mx-0">
      <Col sm={3}>
        <Landing />
      </Col>
      <Col sm={9}>
        <Station id="app" />
      </Col>
    </Row>
  );
}

export default App;
