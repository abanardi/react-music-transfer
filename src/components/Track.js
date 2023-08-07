import React from 'react'
import './Track.css'

export default function Track({imageId, name, artist}) {


  return (
    <div className='track'>
        <div className='track-image'></div>
        <div className='track-name'>{name}</div>
        <div className='track-artist'>{artist}</div>
    </div>
  )
}
