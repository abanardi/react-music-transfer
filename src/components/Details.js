import React from 'react';
import './Details.css';
import Track from './Track';

export default function Details({ name, songs }) {
  const testDialog = () =>{
    window.alert('You just clicked the add to music button');
  }

  const tracks = [
    {
      key: 1,
      name: 'Between the Hammer and the Anvil',
      artist: 'Judas Priest',
    },
    {
      key: 2,
      name: 'Knocking at Your Back Door',
      artist: 'Deep Purple',
    },
    {
      key: 3,
      name: 'Contemptress',
      artist: 'Motionless in White',
    },
    {
      key: 4,
      name: 'Complicated',
      artist: 'Avril Lavigne',
    },
    {
      key: 5,
      name: 'Love Story',
      artist: 'Taylor Swift',
    },
    {
      key: 6,
      name: 'Runaway',
      artist: 'Against the Current',
    },
    {
      key: 7,
      name: 'The Downfall of Us All',
      artist: 'A Day To Remember',
    },
    {
      key: 8,
      name: 'Unity',
      artist: 'Shinedown',
    },
    {
      key: 9,
      name: 'Monster',
      artist: 'Starset',
    },
    {
      key: 10,
      name: 'Dear Agony',
      artist: 'Breaking Benjamin',
    },
    {
      key: 11,
      name: 'Hearts Burst Into Fire',
      artist: 'Bullet For My Valentine',
    },
  ];
  return (
    <div>
      <div className="playlist-header-container">
        <div className="playlist-header">
          <div className="playlist-art"></div>
          <h1 className="playlist-title">My Playlist 7</h1>
        </div>
        <button className='transfer-to-apple-music-button' onClick={testDialog}>Create Playlist in Apple Music</button>
      </div>

      <div className="tracks">
        {tracks.map((track) => {
          return <Track key={track.key} name={track.name} artist={track.artist} />;
        })}
      </div>
    </div>
  );
}
