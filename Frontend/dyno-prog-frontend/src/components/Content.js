import Box from "@mui/material/Box";
import Button from "@mui/material/Button";

const Content = () => {
  return (
    <Box sx={{ 
        display: 'flex',
        justifyContent: 'center',
        "& button": { m: 1 } ,
        }}>
      <Button
        variant="contained"
        size="large"
        sx={{
          backgroundColor: "#FF6B1A",
          fontWeight: 900,
          "&:hover": {
            backgroundColor: "darkred",
          },
        }}
      >
        Generate
      </Button>
    </Box>
  );
};

export default Content;
