import React from 'react'
import { Link } from 'react-router-dom'
import paths from '../utils/paths'
import Button from './Button'

export default function Header(props) {
  return (
    <div className={'header'}>
        {paths.map(route => (
            (props.path !== route.path) ? 
            <Link key={route.path} to={route.path}> 
              <Button title={route.name}>
              </Button>
            </Link> 
            : console.log()
        ))}
    </div>
  )
}
