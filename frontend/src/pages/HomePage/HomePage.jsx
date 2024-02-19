import React from 'react'
import Header from '../../UI/Header';
import { useLocation } from 'react-router-dom'


export default function HomePage() {
  return (
    <div className={'home'}>
      <Header path={useLocation().pathname}></Header>
      It is a homepage
    </div>
  );
};