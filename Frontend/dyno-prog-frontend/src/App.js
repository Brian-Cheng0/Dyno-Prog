import "./App.css";
import Nav from "./components/Nav";
import Content from "./components/Content";
import styled from "styled-components";

const LogoDiv = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 400px;
  background-color: #ffffff;
  background-image: radial-gradient(#000 20%, transparent 1%),
    radial-gradient(#000 10%, transparent 1%);
  background-size: 10px 10px;
  background-position: 0 0, 30px 30px;
  background-repeat: repeat;
`;

function App() {
  return (
    <div className="App">
      <Nav />
      <LogoDiv>
        <Content />
      </LogoDiv>
    </div>
  );
}

export default App;
