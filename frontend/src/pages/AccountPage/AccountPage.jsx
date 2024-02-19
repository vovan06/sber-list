import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import Header from '../../UI/Header';


var getCookies = function(){
  var pairs = document.cookie.split(";");
  var cookies = {};
  for (var i=0; i<pairs.length; i++){
    var pair = pairs[i].split("=");
    cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join('='));
  }
  return cookies;
}

async function getActivities(link, setter) {
  let request = await axios.get(link);
  let data = await request.data;
  await console.log(data)
  await setter(data)

};

export default function AccountPage() {
  const [user, setUser] = useState({});
  const [products, setProducts] = useState({});
  const [tasks, setTasks] = useState({});
  const [subtasks, setSubtasks] = useState({});

  useEffect(()=>{
    setUser(getCookies());
    console.log(user)
  }, [])
  return (
    <div>
      <Header path={useLocation().pathname}></Header>
      {user.name} {user.patronymic} {user.surname};
      {user.email}
      <button onClick={()=>(getActivities(`http://alexander.kizimenko.fvds.ru/api/v1/docs/projects/by/user/${user.id}/`, setProducts))}>My projects</button>
      <button onClick={()=>(getActivities(`http://alexander.kizimenko.fvds.ru/api/v1/docs/task/main/by/user/${user.id}/`, setProducts))}>Tasks</button>
      <button onClick={()=>(getActivities(`http://alexander.kizimenko.fvds.ru/api/v1/docs/subtasks/by/user/${user.id}/`, setProducts))}>Sub tasks</button>
    </div>
  )
}
