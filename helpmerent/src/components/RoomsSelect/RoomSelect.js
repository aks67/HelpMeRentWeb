import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';


function RoomSelect() {
    const [bedrooms, setBedrooms] = useState('1');


    const handleRoomsChange = (event) => {
        const bdr = event.target.value;
        setBedrooms(bdr);
        console.log(bdr);
    };

    return (
        <div>
          <Select
            label="Number of Bedrooms"
            variant="outlined"
            value={bedrooms}
            onChange={handleRoomsChange}

          >
            <MenuItem value={1}>1 Bedroom</MenuItem>
            <MenuItem value={2}>2 Bedrooms</MenuItem>
            <MenuItem value={3}>3 Bedrooms</MenuItem>
            <MenuItem value={4}>4+ Bedrooms</MenuItem>
          </Select>
        </div>
      );

}



export default RoomSelect;