import styled from 'styled-components';
// Creating a styled div
const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
`;

// Creating a styled button
const StyledButton = styled.button`
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  
  &:hover {
    background-color: #0056b3;
  }
`;

const Nav = () => {
    return (
      <div>
        <img src="/img/Logo.png" alt="logo" />
        <ul>
          <li>option1</li>
        </ul>
      </div>
    );
  };

export default Nav;
