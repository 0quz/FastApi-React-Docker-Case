import { useState, useEffect } from "react";
import axios from "axios";
import Select from 'react-select';
import ImageSlider from '../components/ImageSlider.js'


export default function RandomMatch() {
	const [app,  setApp] = useState([])
    const [screenshot,  setScreenshot] = useState([])
    const [screenshot2,  setScreenshot2] = useState([])
    const [lastAppId,  setLastApp] = useState()
    const [breakFlag,  setBreakFlag] = useState(false)

    useEffect(() => {
        axios.get("http://0.0.0.0:8080/get_apps")
        .then(res => {
            if (res.data.sucess){
                setApp(res.data.apps);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    }, []);

    const handleChange = (e) => {
        /*
        // If the random button is used once. This flag will prevent triggering the next one.
        if (breakFlag) {
            return
        }
        */
        let appID = e.value
        if (!appID) {
            appID = app[Math.floor(Math.random() * app.length)].id
        }
        // if you remove e.value in the if statements you will be able to use the dropdown menu for number two-block.
        if (!lastAppId && e.value) { // first e.value
            axios.post("http://0.0.0.0:8080/get_screenshots_by_app_id",
            {
                appid: appID
            }
            ).then(res => {
                if (res.data.sucess){
                    setScreenshot(res.data.screenshots)
                    setLastApp(appID)
                }
            }).catch((err) => {
                console.log(err);
            });
        }
        // if you remove e.value in the if statements you will be able to use the dropdown menu for number two-block.
        if (lastAppId && !e.value){ // second e.value
            let index = Math.floor(Math.random() * app.length)
            appID = app[index].id
            if (lastAppId === appID){
                app.splice(index, 1);
                appID = app[Math.floor(Math.random() * app.length)].id
            }
            axios.post("http://0.0.0.0:8080/get_screenshots_by_app_id",
            {
                appid: appID
            }
            ).then(res => {
                if (res.data.sucess){
                    setScreenshot2(res.data.screenshots)
                    setBreakFlag(true)
                }
            }).catch((err) => {
                console.log(err);
            });
        }
    }

    const apps = []
    {app.map((app) => (
        apps.push({ text: app.name, icon: <img src={'data:image/png;base64,'+ app.icon} style={{height: '25px', width: '25px'}}/>, value: app.id })
    ))}

    const customFilter = (apps, searchText) => {
        if (
          apps.data.text.toLowerCase().includes(searchText.toLowerCase())
        ) {
          return true;
        } else {
          return false;
        }
      }

    const screenshots = []
    {screenshot.map((screenshot) => (
        screenshots.push({image:screenshot.screenshot})
    ))}

    const screenshots2 = []
    {screenshot2.map((screenshot) => (
        screenshots2.push({image:screenshot.screenshot})
    ))}

    return (
        <div style={{marginTop: "25px"}}>
            <div style={{
                position: 'relative',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            }}>
                <div style={{width: '300px'}}>
                    <Select
                        options={apps}
                        onChange={handleChange}
                        getOptionLabel={e => (
                            <div style={{ alignItems: 'center' }}>
                            {e.icon}
                            <span style={{ marginLeft: 10 }}>{e.text}</span>
                            </div>
                        )}
                        filterOption={customFilter}
                    />
                </div>
                <button onClick={handleChange} style={{marginLeft: '20px'}}>Randomize</button>
            </div>
            <div>
                <div style={{float: 'left', marginLeft: '500px'}}>
                    <h2>First Game</h2>
                    <ImageSlider slides={screenshots} />
                </div>
                <div style={{float: 'right', marginRight: '500px'}}>
                    <h2>Second Game</h2>
                    <ImageSlider slides={screenshots2} />
                </div>
            </div>
        </div>
    )
	
}