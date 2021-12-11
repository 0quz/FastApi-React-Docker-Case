import { useState } from "react";
import axios from "axios";

export default function WebpConverter() {
	 const [file,  setFile] = useState()
     
     const handleChange = (e) =>{
        console.log(e.target.files[0])
        const formData = new FormData();
        formData.append(
            "img",
            e.target.files[0],
            e.target.files[0].name
          );
        axios.post("http://0.0.0.0:8080/webpconverter", formData, { responseType: 'blob' })
        .then(res => {
            console.log(res)
            //setFile(res.data)
            setFile(URL.createObjectURL(res.data))
          })
     }
     
     return (
         <div style={{marginTop: "25px"}}>
          <input type="file" onChange={handleChange}/>
          <div>
            <img src={file} style={{height: '800px', width: '800px', marginTop: '25px'}}/>
          </div>
          
        </div>
     )
	
}