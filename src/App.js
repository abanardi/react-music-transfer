import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useEffect } from 'react';
import Album from './components/Album';
import Details from './components/Details';
import Login from './components/Login';

function App() {
  function fetchAPI() {
    axios
      .get('http://localhost:5500/hello')
      .then((response) => console.log(response.data));
  }

  const playlists = [
    {
      key: 1,
      name: 'Chill',
    },
    {
      key: 2,
      name: 'My Playlist 7',
    },
    {
      key: 3,
      name: 'My Inner Yash',
    },
    {
      key: 4,
      name: 'Hard Rock',
    },
    {
      key: 5,
      name: 'Garbage Tester Playlist',
    },
    {
      key: 6,
      name: 'The worst playlist imaginable',
    },
  
  ];


  return (
    <div className="App">
      <Login/>

      <h1 className='app-title' onClick={fetchAPI}>Welcome to the playlist transfer tool</h1>
      <div className="app-container">
        <div className="album-container">
          {playlists.map((playlist) => {
            return <Album key={playlist.key} name={playlist.name}/>;
          })}
        </div>
      </div>

      <Details/>



    </div>
  );
}

export default App;
