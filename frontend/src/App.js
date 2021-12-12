import './App.css';
import Login from './screens/Login.js'
import WebpConverter from './screens/WebpConverter.js'
import RandomMatch from './screens/RandomMatch.js'
import { useState } from "react";

function App() {
  const [showPage, setShowPage] = useState();

  const selectPage = e => {
    if (e.target.value === "Login"){
      setShowPage(<Login />)
    } else if (e.target.value === "WebpConverter") {
      setShowPage(<WebpConverter />)
    } else if (e.target.value === "RandomMatch") {
      setShowPage(<RandomMatch />)
    }
  }

  return (
    <div className="App" style={{marginTop: '50px'}}>
          <button onClick={selectPage} value="Login">Try Login</button>
          <button onClick={selectPage} value="WebpConverter" style={{marginLeft: '25px', marginRight: '25px'}}>Try WebpConverter</button>
          <button onClick={selectPage} value="RandomMatch">Try RandomMatch</button>
          {showPage}
    </div>
  );
}

export default App;