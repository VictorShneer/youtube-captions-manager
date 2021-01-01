import React, {useState, useEffect} from 'react';
import YouTube from 'react-youtube';
import './App.css';

function App() {
  const [value, setValue] = useState(''); 
  const [videoId, setVideoId] = useState(''); 
  const [startSec, setStartSec] = useState(0); 
  
  const opts = {
    height: '390',
    width: '640',
    playerVars: {
      // https://developers.google.com/youtube/player_parameters
      autoplay:1,
      start:  startSec,
    },
  };

  function handleChange(event) {
    setValue(event.target.value)
  }

  function handleSubmit(event) {
    fetch('/api/tickle/'+value).then(res=>res.json()).then(data=>{
      setStartSec(parseInt(data.phrase.start));
      console.log(opts)
      console.log(opts.playerVars.start)
      setVideoId(data.link);
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

        <form onSubmit={handleSubmit}>
          <label>
            <input type="text" value={value} onChange={handleChange} />
          </label>
          <input type="submit" value="Отправить" />
        </form>
        <p><YouTube videoId={videoId} opts={opts} onReady={onReady} />;</p>
      </div>
    );
}

export default App;

