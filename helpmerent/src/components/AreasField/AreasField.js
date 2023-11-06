import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Chip from '@mui/material/Chip';

function TagInput() {
  const [tags, setTags] = useState([]);
  const [inputValue, setInputValue] = useState('');

  // Handle changes to the input field
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  // Handle adding a tag when Enter is pressed
  const handleInputKeyPress = (event) => {
    if (event.key === 'Enter' && inputValue.trim() !== '') {
      setTags([...tags, inputValue.trim()]);
      setInputValue('');
    }
  };

  // Handle removing a tag
  const handleDelete = (tagToDelete) => {
    setTags(tags.filter((tag) => tag !== tagToDelete));
  };

  return (
    <div>
      {tags.map((tag, index) => (
        <Chip
          key={index}
          label={tag}
          onDelete={() => handleDelete(tag)}
        />
      ))}
      <TextField
        label="Add Postcodes"
        variant="outlined"
        value={inputValue}
        onChange={handleInputChange}
        onKeyPress={handleInputKeyPress}
        fullWidth
        placeholder="Press Enter to add Posts"
      />
    </div>
  );
}

export default TagInput;
