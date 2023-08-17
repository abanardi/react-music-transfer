import './Login.css';
import axios from 'axios';

import React from 'react';

export default function Login() {
  const getUrl = () => {
    console.log(window.location.href);
  };

  const dummyTesting = async () => {
    const response = await axios.get('http://localhost:5500/step_one', {params: {
        client_id: '7d16366b3ae34465a0561cd91120c3e6',
        client_secret: 'c3e0c461a745496b8e270863a7efb90a',
        redirect_uri: 'http://localhost:3000/',
      }}, );
    const navigationUrl = response.data;
    
    console.log(navigationUrl)
    
    
    // const url = window.location.href.toString();
    console.log('What');
  };

  const getPlaylistIsrc = () => {
    console.log('We will figure this out later');
  };

  return (
    <div>
      <h1 className='login-title'> Welcome, please click here after authentication</h1>
      <button onClick={dummyTesting}> Click me! </button>
      <button onClick={getPlaylistIsrc}>
        This is a test button to make sure that the API calls are consistent
      </button>
    </div>
  );
}
