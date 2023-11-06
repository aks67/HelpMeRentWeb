import React, { useState, useEffect } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

function BudgetField() {
    
    const [budget, setBudget] = useState('');

    const handleBudgetChange = (event) => {
        const newBudgetValue = event.target.value;
        setBudget(newBudgetValue);
        console.log(newBudgetValue)
      };

    return (
        <div>
          <TextField
            id="budget-input"
            label="Enter Your Budget"
            variant="outlined"
            type="Search Field"
            value={budget}
            onChange={handleBudgetChange}
            placeholder="Enter your budget rounded to 50"
          />
        </div>
      );
}

export default BudgetField;