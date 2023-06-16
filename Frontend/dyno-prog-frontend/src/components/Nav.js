import styled from "styled-components";
const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
`;

const StyledList = styled.ul`
display: flex;
align-items: center;
list-style-type: none;
padding: 0;
`;

const StyledListItem = styled.li`
padding: 50px;
cursor: pointer;
font-family: "Montserrat", sans-serif;
font-weight: 800;
font-size: 16px; // Added font size
transition: color 0.3s ease-in-out; // Added transition for hover effect
&:hover {
  color: aqua;
}
`;

const Nav = () => {
  return (
    <Container>
      <StyledList>
        <StyledListItem>BNF</StyledListItem>
        <StyledListItem>AST</StyledListItem>
        <StyledListItem>Lexer</StyledListItem>
        <StyledListItem>Parser</StyledListItem>
      </StyledList>
    </Container>
  );
};

export default Nav;
