import React, { useState } from 'react'
import axios from "axios";

export default function Login () {
  // state tanimlari
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  
  const handleChange = (event) => {
    // user name ve password duruma gore kendi statelerine kaydedilir.
    if (event.target.name === "username"){
      setUserName(event.target.value)
    } else {
      setPassword(event.target.value)
    }
  };

  const handleSubmit = (event) => {
    //form doldurulup sumbit butonuna basildiginda user name ve password endpointe bir istek olarak gider.
    axios
      .post(
        "http://0.0.0.0:8080/login",
        {
          username: userName,
          password: password
        }
      )
      .then(response => {
        setMessage(response.data.message)
      })
      .catch(error => {
        console.log("login error", error);
      });
    event.preventDefault(); // form submit edildikten sonra ekran yenilenmesini onlemek
  };
    return (
      // username, password input tanimlari ve sumbit button tanimi
      <div>
        <form onSubmit={handleSubmit} style={{marginTop: '100px', marginBottom: '25px'}}>
          <input
            name="username"
            placeholder="Enter Username"
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
        <span style={{color: 'red', fontWeight: 'bold'}}> {message} </span>
      </div>
    );
}