import React from 'react';
import './Album.css'


export default function Album({name, imageId}) {
  return <div className="album-element">
    <div className='album-art'>
      
    </div>
    <div className='album-details'>
        <p className='album-name'>{name}</p>
    </div>

  </div>;
}
