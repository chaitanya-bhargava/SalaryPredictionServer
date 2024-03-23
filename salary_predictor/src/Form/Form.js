import React, { useState } from 'react';
import './Form.css'
import { TextField, Button, MenuItem, FormControl, InputLabel, Select, Typography } from '@mui/material';

const FormComponent = () => {
  const [age, setAge] = useState('');
  const [experience, setExperience] = useState('');
  const [gender, setGender] = useState('');
  const [educationLevel, setEducationLevel] = useState('');
  const [responseText, setResponseText] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    var newGender;
    var newEducationLevel;
    switch(gender){
        case 'Male':
            newGender='0'
            break;
        case 'Female':
            newGender='1'
            break;
        default:
            newGender='0'
            break;
    }
    switch(educationLevel){
        case "Bachelor's":
            newEducationLevel='0'
            break;
        case "Master's":
            newEducationLevel='1'
            break;
        case "Phd":
            newEducationLevel='2'
            break;
        default:
            newEducationLevel='0'
            break;
    }
    // Prepare query parameters
    const queryParams = new URLSearchParams({
      age: age,
      yearsExperience: experience,
      gender: newGender,
      educationLevel: newEducationLevel
    }).toString();

    // Construct URL with query parameters
    const url = `http://127.0.0.1:5000/predict?${queryParams}`;

    try {
      const response = await fetch(url);
      const data = await response.json();
      const prediction=data[0].prediction
      const newPrediction=Math.trunc(prediction)
      setResponseText(`Your salary will be around ₹${newPrediction} per month`);
    } catch (error) {
      console.error('Error:', error);
      setResponseText('Error fetching data');
    }
  };

  return (
    <div className='form-container'>
      <h1>Salary Prediction</h1>
      <form onSubmit={handleSubmit} >
        <TextField
          label="Age"
          variant="outlined"
          fullWidth
          value={age}
          onChange={(e) => setAge(e.target.value)}
          margin="normal"
          type="text"
          required
        />
        <FormControl variant="outlined" fullWidth margin="normal" required>
          <InputLabel>Gender</InputLabel>
          <Select
            value={gender}
            onChange={(e) => setGender(e.target.value)}
            label="Gender"
            required
          >
            <MenuItem value="Male">Male</MenuItem>
            <MenuItem value="Female">Female</MenuItem>
          </Select>
        </FormControl>
        <FormControl variant="outlined" fullWidth margin="normal" required>
          <InputLabel>Level of Education</InputLabel>
          <Select
            value={educationLevel}
            onChange={(e) => setEducationLevel(e.target.value)}
            label="Level of Education"
            required
          >
            <MenuItem value="Bachelor's">Bachelor's</MenuItem>
            <MenuItem value="Master's">Master's</MenuItem>
            <MenuItem value="Phd">Phd</MenuItem>
          </Select>
        </FormControl>
        <TextField
          label="Years of Experience"
          variant="outlined"
          fullWidth
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
          margin="normal"
          type="text"
          required
        />
        <Button type="submit" variant="contained" color="primary" sx={{marginTop:"20px", textAlign:"center"}}>
          Submit
        </Button>
      </form>
      <br/>
      <br/>
      <br/>
      {responseText && (
        <div>
          <Typography variant="h5" textAlign={'center'}>
            {responseText}
          </Typography>
        </div>
      )}
    </div>
  );
};

export default FormComponent;
