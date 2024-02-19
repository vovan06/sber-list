import React from 'react'
import { useLocation, useNavigate } from 'react-router-dom';
import Button from '../../UI/Button';
import Header from '../../UI/Header';

function deleteAllCookies(navigate, path) {
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        console.log(cookie)
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    };
    console.log(document.cookie);
    navigate(path);
};

export default function LogoutPage() {
   let navigate = useNavigate();
  
   return (
    <div>LogoutPage
      <Header path={useLocation().pathname}></Header>

    <button onClick={() => deleteAllCookies(navigate, '/login')}>Logout</button>        
    </div>
  )
}
