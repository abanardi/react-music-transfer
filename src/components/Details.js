import React from 'react';
import './Details.css';
import Track from './Track';

export default function Details({ name, songs }) {
  const testDialog = () =>{
    window.alert();
  }

  const tracks = [
    {
      name: 'Between the Hammer and the Anvil',
      artist: 'Judas Pries',
    },
    {
      name: 'Knocking at Your Back Door',
      artist: 'Deep Purple',
    },
    {
      name: 'Contemptress',
      artist: 'Motionless in White',
    },
    {
      name: 'Complicated',
      artist: 'Avril Lavigne',
    },
    {
      name: 'Love Story',
      artist: 'Taylor Swift',
    },
    {
      name: 'Runaway',
      artist: 'Against the Current',
    },
    {
      name: 'The Downfall of Us All',
      artist: 'A Day To Remember',
    },
    {
      name: 'Unity',
      artist: 'Shinedown',
    },
    {
      name: 'Monster',
      artist: 'Starset',
    },
    {
      name: 'Dear Agony',
      artist: 'Breaking Benjamin',
    },
    {
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
          <button className='transfer-to-apple-music-button' onClick={testDialog}>Create Playlist in Apple Music</button>
        </div>
      </div>

      <div className="tracks">
        {tracks.map((track) => {
          return <Track name={track.name} artist={track.artist} />;
        })}
      </div>
    </div>
  );
}
