import React from 'react'
import { Link } from 'react-router-dom'
import '../Styles/nav.css'
import { useHistory } from 'react-router-dom';



export default function Navbar() {
    const history = useHistory();
    return (
        <div className="nav-container">
            <div className="logo">
                <h3 onClick={() => history.push('/')}>U-Match</h3>
            </div>
            <div className="options">
                <h3 onClick={() => history.push('/')}>Home</h3>
                <Link onClick={() => history.push('/profile')} className="nav-item"><h3>Profile</h3></Link>
                <h3>Logout</h3> 
            </div>
        </div>
    )
}
