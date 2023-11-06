import React from 'react';
import Button from '@mui/material/Button';


function GoButton({ onClick }) {
  return (
    <Button variant="contained" color="primary" onClick={onClick} size='large'>
      Compute
    </Button>
  );
}

export default GoButton;
