import { useState } from "react";
import axios from "axios";

export default function WebpConverter() {
   // state tanimlari
	 const [img, setImg] = useState()
     
     const handleChange = (e) =>{
        // resim formdata seklinde gonderilir.
        const formData = new FormData();
        formData.append(
            "img",
            e.target.files[0],
            e.target.files[0].name
          );
        axios.post("http://0.0.0.0:8080/webp_converter", formData, { responseType: 'blob' }) // resim blob type olarak dondugu icin bu sekilde bi responsetype var.
        .then(res => {
            // donusturulmus resim dosyasi degiskene kaydedilir.
            setImg(URL.createObjectURL(res.data))
          })
     }
     
     return (
         // Resim input alani ve resim ekranda gosterme islemleri yapilir.
         <div style={{marginTop: "25px"}}>
          <input type="file" onChange={handleChange}/>
          <div>
            <img src={img} style={{height: '800px', width: '800px', marginTop: '25px'}} alt='Webp'/>
          </div>
          
        </div>
     )
	
}