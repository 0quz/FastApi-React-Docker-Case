import React, { useState } from 'react'
import axios from "axios";

export default function Login () {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  
  const handleChange = (event) => {
    if (event.target.name === "username"){
      setUserName(event.target.value)
    } else {
      setPassword(event.target.value)
    }
  };

  const handleSubmit = (event) => {
    axios
      .post(
        "http://0.0.0.0:8080/login",
        {
          username: userName,
          password: password
        },
        { withCredentials: true }
      )
      .then(response => {
        setErrorMessage(response.data.message)
      })
      .catch(error => {
        console.log("login error", error);
      });
    event.preventDefault();
  };
    return (
      <div>
        <form onSubmit={handleSubmit} style={{marginTop: '100px', marginBottom: '25px'}}>
          <input
            name="username"
            placeholder="EnterUsername"
            value={userName}
            onChange={handleChange}
            style={{marginRight: '10px'}}
            required
          />

          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            value={password}
            style={{marginRight: '10px'}}
            onChange={handleChange}
            required
          />
          <button type="submit">Login</button>
        </form>
        <span style={{color: 'red', fontWeight: 'bold'}}> {errorMessage} </span>
      </div>
    );
}