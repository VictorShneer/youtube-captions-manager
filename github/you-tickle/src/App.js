import React, {useState, useEffect} from 'react';
import YouTube from 'react-youtube';
import './App.css';




function App() {
  const [value, setValue] = useState(''); 
  const [videoId, setVideoId] = useState(''); 
  const [startSec, setStartSec] = useState(0); 
  const [log, setLog] = useState(''); 
  const [response, setResponse] = useState('');


  const opts = {
    height: '390',
    width: '640',
    playerVars: {
      // https://developers.google.com/youtube/player_parameters
      autoplay:1,
      start:  startSec,
      controls: '0',
    },
  };

  function handleChange(event) {
    setValue(event.target.value)    
  }

  function handleSubmit(event) {
    fetch('/api/tickle/'+value).then(res=>res.json()).then(data=>{
      if(data.captions){
        setResponse(JSON.stringify(data['captions']));
        setStartSec(parseInt(data.captions[0].start));
        setVideoId(data.captions[0].video_id);
        console.log(data.captions[0].video_id);
      }else{
        setResponse(JSON.stringify(data['message']));
      }

    })

    event.preventDefault();
  }

 function onReady(event) {
    // access to player in all event handlers via event.target
    event.target.pauseVideo();
    // console.log('akolbes!')
    // event.target.playVideo();
  }

    return (
      <div>
        <div className="topnav">
         <div class="search-container">
          <form onSubmit={handleSubmit}>
            <label>
              <input type="text" value={value} placeholder="Search.." onChange={handleChange} />
            </label>
            <input type="submit" value="Отправить" />
          </form>
          </div>
        </div>
        <p>{response}</p>
        <YouTube videoId={videoId} opts={opts} onReady={onReady}/>
      </div>
    );
}

export default App;

